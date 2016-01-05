# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import redis
import multiprocessing
import json
import config
import util
import sys
sys.path.append("appstores")
class Detail_page_handler(object):
    def __init__(self , logger = None, **redis_kwargs) :
        self.logger = logger
        self.rd = redis.Redis(**redis_kwargs)
        self.lock = multiprocessing.RLock()
        self.url_rd = redis.Redis(db = 11, **redis_kwargs)
        self.phantomjs_webdrivers = []
        self.processes = []

    def prepare_args(self, args_str):
        try:
            args = json.loads(args_str)
        except (TypeError, ValueError):
            util.write_log_error(self.lock, self.logger, 'can not parse %s to json args.'%(args_str))
            return None
        if not 'level' in args:
            args['level'] = 'low'
        if not 'source' in args:
            util.write_log_error(self.lock, self.logger, 'source not found.')
            return None
        if not 'detail_page_url' in args:
            util.write_log_error(self.lock, self.logger, 'detail_page_url not found.')
            return None
        # if not 'phantomjs_user_agent' in args:
        #     args['phantomjs_user_agent'] = config.PHANTOMJS_USER_AGENT
        if not 'message_type' in args:
            args['message_type'] = config.MESSAGE_TYPE_NORMAL
        return args

    def push_message(self, out_json_message):
        next_queue = out_json_message['next_queue']
        del out_json_message['next_queue']
        return self.rd.lpush(next_queue, json.dumps(out_json_message))

    def crawl(self, args, browser):
        source = args['source']
        detail_page_url = args['detail_page_url']
        try:
            appstore_modual = __import__(source)
        except ImportError:
            util.write_log_error(self.lock, self.logger, "can not find " + source + ".py in configured appstores")
            return False
        appstore_class = appstore_modual.Store()
        if self.url_rd.exists(util.get_MD5(detail_page_url)):
            util.write_log_warn(self.lock, self.logger, "detail_page_url:" + detail_page_url + "was crawled in past %d seconds"%(config.CRAWLED_URL_REDIS_TIMEOUT))
            return False
        browser.desired_capabilities["phantomjs.page.settings.userAgent"] = appstore_class.PHANTOMJS_USER_AGENT
        util.browser_get_url(browser, detail_page_url)
        download_url = appstore_class.get_download_url(browser)
        if download_url is None:
            util.write_log_error(self.lock, self.logger, "详情页: " + detail_page_url + " 找不到download_url")
            return False
        out_json_message = appstore_class.make_detail2download_json_message(browser)
        out_json_message['detail_url'] = detail_page_url
        out_json_message['download_url'] = download_url
        if args['level'] = 'high':
            out_json_message['next_queue'] = config.HIGH_DOWNLOAD_QUEUE
        else:
            out_json_message['next_queue'] = config.LOW_DOWNLOAD_QUEUE
        out_json_message['level'] = args['level']
        out_json_message['message_type'] = args['message_type']
        util.write_log_info(self.lock, self.logger,"SUCCESS : detail_page_url: %s crawled"%(detail_page_url))
        self.url_rd.set(util.get_MD5(detail_page_url),1)
        self.url_rd.expire(util.get_MD5(detail_page_url), config.CRAWLED_URL_REDIS_TIMEOUT)
        return self.push_message(out_json_message)

    def normal(self, args, browser):
        util.write_log_warn(self.lock, self.logger, '"normal" message type did nothing.')
        return True

    def do_work(self, message, browser):
        util.random_sleep()
        args = self.prepare_args(message)
        if args is None:
            return
        return eval('self.'+args['message_type'])(args, browser)

    def work_process(self, browser):
        util.write_log_info(self.lock, self.logger, 'new detail_page_handler process started')
        while 1:
            try:
                message = self.rd.brpop([config.HIGH_DETAIL_PAGE_HANDLE_QUEUE, config.LOW_DETAIL_PAGE_HANDLE_QUEUE],0)
                util.write_log_info(self.lock, self.logger, 'received new nessage: %s'%(message[1]))
                self.do_work(message[1], browser)
            except Exception:
                import traceback
                util.write_log_error(self.lock, self.logger,"detail_page_handler process catched exception." + traceback.print_exc())

    def launch(self):
        while len(self.phantomjs_webdrivers)<config.MAX_DETAIL_PAGE_HANDLER_PROCESS_NUM:
            phantomJS_browser = util.start_phantomJS_browser()
            if phantomJS_browser:
                self.phantomjs_webdrivers.append(phantomJS_browser)
                process = multiprocessing.Process(target = self.work_process, args=(phantomJS_browser, ))
                process.daemon = True
                self.processes.append(process)
                process.start()
            else:
                util.write_log_error(self.lock, self.logger,"phantomJS start failed.")

    def quit(self):
        self.rd.save()
        self.url_rd.save()
        for process in self.processes:
            process.terminate()
            process.join()
        for browser in self.phantomjs_webdrivers:
            browser.quit()
        sys.exit(-1)
##########################################################################################
def main(argv):
    import socket
    socket.setdefaulttimeout(config.SOCKET_TIMEOUT)
    logger = None
    if config.LOGGER_ENABLED:
        logger = util.initLog(config.LOGGER_NAME_DETAIL_PAGE_HANDLER)
    multiprocessing.current_process().name = 'detail_page_handler_process_main'
    detail_page_handler = Detail_page_handler(logger = logger, host = config.REDIS_HOST, port = config.REDIS_PORT)
    util.write_log_info(detail_page_handler.lock, detail_page_handler.logger,"[+]start detail_page_handler...")
    detail_page_handler.launch()
    try:
        content=raw_input()
        while content != 'exit':
            content=raw_input()
    except KeyboardInterrupt:
        pass
    util.write_log_info(detail_page_handler.lock, detail_page_handler.logger,"user determined detail_page_handler")
    detail_page_handler.quit()

if __name__ == '__main__':
    main(sys.argv)