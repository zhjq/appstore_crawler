import time
import threading
import logging
import requests
import redis
import json
import sys
import os
from contextlib import closing

import util
import config

class Downloader(object):
    def __init__(self , logger = None, **redis_kwargs) :
        self.logger = logger
        self.rd = redis.Redis(**redis_kwargs)
        self.url_rd = redis.Redis(db = 12, **redis_kwargs)
        self.lock = threading.RLock()

    def prepare_args(self, args_str):
        try:
            args = json.loads(args_str)
        except (TypeError, ValueError):
            util.write_log_error(self.lock, self.logger, 'can not parse %s to json args.'%(args_str))
            return None
        if not 'download_url' in args:
            util.write_log_error(self.lock, self.logger, 'download_url not found.')
            return None
        if not 'level' in args:
            args['level'] = 'low'
        if not 'method' in args:
            args['method'] = config.REQUESTS_ACTION_GET
        if not 'data' in args:
            args['data'] = None
        if not 'request_headers' in args:
            args['request_headers'] = config.REQUEST_HEADERS
        if not 'download_cookie_producer' in args:
            args['download_cookie_producer'] = None
        if not 'download_folder' in args:
            args['download_folder'] = config.DEFAULT_DOWNLOAD_FOLDER
        if not 'download_file_name' in args:
            args['download_file_name'] = self.DEFAULT_DOWNLOAD_FILE_NAME()
        if not 'download_file_type' in args:
            args['download_file_type'] = config.DEFAULT_DOWNLOAD_FILE_TYPE
        if not 'target_folder' in args:
            args['target_folder'] = config.DEFAULT_FILE_HANDLE_FOLDER
        if not 'message_type' in args:
            args['message_type'] = config.MESSAGE_TYPE_NORMAL
        return args

    def prepare_download_session(self, session_producer, request_headers):
        session = requests.Session()
        if session_producer is None:
            return session
        if 'url' not in session_producer:
            return session
        if 'method' not in session_producer:
            session_producer['method'] = 'GET'
        if 'data' not in session_producer:
            session_producer['data'] = None
        if url in session_producer:
            session.request(method = session_producer['method'] or 'GET', url = session_producer['url'], data = session_producer['data'], headers = request_headers, timeout = config.REQUESTS_TIMEOUT)
        return session

    def _check_response(self, response, file_type):
        if response is None:
            return 'response is None'
        if response.status_code != 200:
            return 'status_code of last response is not 200'
        if  'content-type' in response.headers:
            if not response.headers['content-type'] in config.FILE_TYPE[file_type]['content-type']:
                return 'content-type of last response is not wanted'
        return 'success'

    def _record_history(self, url, response):
        download_redirect_urls = []
        download_redirect_urls.append(url)
        for r in response.history:
            if 'location' in r.headers:
                download_redirect_urls.append(r.headers['location'])
        return download_redirect_urls

    def DEFAULT_DOWNLOAD_FILE_NAME(self):
        return str(threading.currentThread().ident)+'_'+str(time.time())

    def _combine_file_name(self, folder = None, file_name = None,  file_type = None):
        if folder is None:
            folder = config.DEFAULT_DOWNLOAD_FOLDER
        if file_name is None:
            file_name = self.DEFAULT_DOWNLOAD_FILE_NAME()
        if file_type is None:
            file_type = config.DEFAULT_DOWNLOAD_FILE_TYPE
        return folder+file_name+config.FILE_TYPE[file_type]['extension_filename']

    def write_content_to_file(self, content, file_name):
        if content is None:
            return 'content of response is None'
        if file_name is None:
            file_name = self._combine_file_name()
        try:
            open(file_name, 'wb').write(content)
        except Exception as e:
            return 'Exception when write to %s. info: %s'%(file_name, e)
        else:
            return 'success'

    def is_url_need_to_download(self, download_url, response, target_folder, download_file_type):
        md5 = util.get_MD5(download_url)
        if 'content-md5' in response.headers:
            apk_md5 = response.headers['content-md5']
            if os.exists(target_folder + 'cell-' + apk_md5[:2] + '/' + apk_md5 +config.FILE_TYPE[download_file_type]['extension_filename']):
                return 'file with same md5 exists'
        if not self.url_rd.exists(md5):
            return 'yes'
        if 'last-modified' in response.headers:
            if response.headers['last-modified'] != self.url_rd.get(md5):
                return 'yes'
            else:
                return 'not modified'
        else:
            return ' has crawled in past %d seconds'%(config.CRAWLED_URL_REDIS_TIMEOUT)

    def put_download_url_into_redis(self, download_url, response):
        md5 = util.get_MD5(download_url)
        if 'last-modified' in response.headers:
            self.url_rd.set(md5, response.headers['last-modified'])
        else:
            self.url_rd.set(md5, 1)
            self.url_rd.expire(md5, config.CRAWLED_URL_REDIS_TIMEOUT)
        return

    def download(self, session, args):
        download_url = args['download_url']
        if download_url is None:
            return 'download_url is None', []
        method, data, request_headers,  download_folder, download_file_name, download_file_type, target_folder = \
            args['method'], args['data'], args['request_headers'], args['download_folder'], args['download_file_name'], args['download_file_type'], args['target_folder']
        if not os.path.exists(download_folder):
            os.mkdir(download_folder)
        download_file_name = self._combine_file_name(download_folder, download_file_name, download_file_type)
        args['file_name'] = download_file_name
        try:
            with closing(session.request(method = method, url = download_url, data = data, headers = request_headers, timeout = config.REQUESTS_TIMEOUT, stream = True)) as response:
                response_check_result = self._check_response(response, download_file_type)
                if response_check_result != 'success':
                    return response_check_result, []
                download_redirect_urls = self._record_history(download_url, response)
                need_to_download = self.is_url_need_to_download(download_redirect_urls[-1], response, target_folder, download_file_type)
                if not need_to_download == 'yes':
                    return "download_url:" + download_redirect_urls[-1] + need_to_download, []
                write_to_file_result = self.write_content_to_file(response.content, download_file_name)
                if write_to_file_result == 'success':
                    self.put_download_url_into_redis(download_redirect_urls[-1], response)
                return write_to_file_result, download_redirect_urls
        except Exception as e:
            return 'Exception when connect to download_url. info: %s'%(e), []

    def _clear_message(self, args):
        del args['download_url']
        del args['method']
        del args['data']    
        del args['download_cookie_producer']
        del args['download_folder']
        del args['download_file_name']
        del args['download_file_type']
        del args['request_headers']

    def push_message(self, out_json_message):
        next_queue = out_json_message['next_queue']
        del out_json_message['next_queue']
        return self.rd.lpush(next_queue, json.dumps(out_json_message))

    def normal(self, args):
        session = self.prepare_download_session(args['download_cookie_producer'], args['request_headers'])
        download_result, download_redirect_urls = self.download(session,args)
        if download_result == 'success':
            util.write_log_info(self.lock, self.logger, "SUCCESS : download_url: %s , file_name: %s "%(args['download_url'] , args['file_name']))
            download_result = True
        else:
            util.write_log_error(self.lock, self.logger, "FAIL : download_url: %s ; reason: %s"%(args['download_url'], download_result))
            download_result = False
        return download_result, download_redirect_urls

    def crawl(self, args):
        download_result, download_redirect_urls = self.normal(args)
        if download_result:
            args['download_redirect_urls'] = download_redirect_urls
            if args['level'] == 'high':
                args['next_queue'] = config.HIGH_FILE_HANDLE_QUEUE
            else:
                args['next_queue'] = config.LOW_FILE_HANDLE_QUEUE
            self._clear_message(args)
            return self.push_message(args)

    def do_work(self, message):
        args = self.prepare_args(message)
        if args is None:
            return
        return eval('self.'+args['message_type'])(args)

    def work_thread(self):
        util.write_log_info(self.lock, self.logger, 'new downloader thread started')
        while 1:
            try:
                message = self.rd.brpop([config.HIGH_DOWNLOAD_QUEUE, config.LOW_DOWNLOAD_QUEUE],0)
                util.write_log_info(self.lock, self.logger, 'received new nessage: %s'%(message[1]))
                self.do_work(message[1])
            except Exception:
                import traceback
                util.write_log_error(self.lock, self.logger, 'downloader thread catched exception.' + traceback.print_exc())

    def launch(self):
        for i in xrange(config.MAX_DOWNLOAD_THREAD_NUM):
            thread = threading.Thread(name = 'downloader_thread_' + `i`, target = self.work_thread)
            thread.setDaemon(True)
            thread.start()
    def quit(self):
        self.url_rd.save()
        self.rd.save()
        sys.exit(-1)
##########################################################################################
def main(argv):
    import socket
    socket.setdefaulttimeout(config.SOCKET_TIMEOUT)
    logger = None
    if config.LOGGER_ENABLED:
        logger = util.initLog(config.LOGGER_NAME_DOWNLOADER)
    threading.current_thread().setName('downloader_thread_main')
    downloader = Downloader(logger = logger, host = config.REDIS_HOST, port = config.REDIS_PORT)
    util.write_log_info(downloader.lock, downloader.logger,"[+]start downloader...")
    downloader.launch()
    try:
        content=raw_input()
        while content != 'exit':
            content=raw_input()
    except KeyboardInterrupt:
        pass
    util.write_log_info(downloader.lock, downloader.logger,"user determined downloader")
    downloader.quit()

if __name__ == '__main__':
    main(sys.argv)

