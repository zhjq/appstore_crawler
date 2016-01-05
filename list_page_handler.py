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

class List_page_handler(object):
    def __init__(self , logger = None, **redis_kwargs) :
        self.logger = logger
        self.rd = redis.Redis(**redis_kwargs)
        self.lock = multiprocessing.RLock()
        self.url_rd = redis.Redis(db = 10, **redis_kwargs)
        self.phantomjs_webdrivers = []
        self.processes = []

    def push_message(self, out_json_message):
        next_queue = out_json_message['next_queue']
        del out_json_message['next_queue']
        return self.rd.lpush(next_queue, json.dumps(out_json_message))

    def push_list_page_message(self, args, list_page_url):
        out_json_message = {}
        out_json_message['source'] = args['source']
        # out_json_message['phantomjs_user_agent'] = args['phantomjs_user_agent']
        out_json_message['list_page_url'] = list_page_url
        out_json_message['message_type'] = args['message_type']
        if args['level'] == 'low':
            out_json_message['next_queue'] = config.LOW_DOWNLOAD_QUEUE
        elif args['level'] = 'high':
            out_json_message['next_queue'] = config.HIGH_DOWNLOAD_QUEUE
        out_json_message['level'] = args['level']
        return self.push_message(out_json_message)

    def push_detail_page_message(self, args, detail_page_urls):
        for detail_page_url in detail_page_urls:
            out_json_message = {}
            out_json_message['source'] = args['source']
            # out_json_message['phantomjs_user_agent'] = args['phantomjs_user_agent']
            out_json_message['detail_page_url'] = detail_page_url
            out_json_message['message_type'] = args['message_type']
            if args['level'] = 'high':
                out_json_message['next_queue'] = config.HIGH_DOWNLOAD_QUEUE
            else:
                out_json_message['next_queue'] = config.LOW_DOWNLOAD_QUEUE
            out_json_message['level'] = args['level']
            self.push_message(out_json_message)
        
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
        if not 'list_page_url' in args:
            util.write_log_error(self.lock, self.logger, 'list_page_url not found.')
            return None
        # if not 'phantomjs_user_agent' in args:
        #     args['phantomjs_user_agent'] = config.PHANTOMJS_USER_AGENT
        if not 'message_type' in args:
            args['message_type'] = config.MESSAGE_TYPE_NORMAL
        return args

    def crawl(self, args, browser):
        source = args['source']
        list_page_url = args['list_page_url']
        try:
            appstore_modual = __import__(source)
        except ImportError:
            util.write_log_error(self.lock, self.logger, "can not find " + source + ".py in configured appstores")
            return False
        appstore_class = appstore_modual.Store()
        if self.url_rd.exists(util.get_MD5(list_page_url)):
            util.write_log_warn(self.lock, self.logger, "list_page_url:" + list_page_url + "was crawled in past %d seconds"%(config.CRAWLED_URL_REDIS_TIMEOUT))
            return False
        browser.desired_capabilities["phantomjs.page.settings.userAgent"] = appstore_class.PHANTOMJS_USER_AGENT
        util.browser_get_url(browser, list_page_url)
        # appstore_class.scroll_down(browser)
        check_more_count = appstore_class.click_checkmore(browser)
        util.write_log_warn(self.lock, self.logger, "列表页: " + list_page_url + "点击checkmore" + str(check_more_count) + "次后找不到checkmore")
        detail_urls = appstore_class.get_detail_urls(browser)
        if len(detail_urls) == 0:
            util.write_log_warn(self.lock, self.logger, "列表页: " + list_page_url + " 找到0个app")
        self.push_detail_page_message(args, detail_urls)
        next_list_page = appstore_class.click_nextpage(browser)
        if next_list_page:
            self.push_list_page_message(args, next_list_page)
        util.write_log_info(self.lock, self.logger,"SUCCESS : list_page_url: %s crawled"%(list_page_url))
        self.url_rd.set(util.get_MD5(list_page_url),1)
        self.url_rd.expire(util.get_MD5(list_page_url), config.CRAWLED_URL_REDIS_TIMEOUT)
        return True

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
        util.write_log_info(self.lock, self.logger, 'new list_page_handler process started')
        while 1:
            try:
                message = self.rd.brpop([config.HIGH_LIST_PAGE_HANDLE_QUEUE, config.LOW_LIST_PAGE_HANDLE_QUEUE],0)
                util.write_log_info(self.lock, self.logger, 'received new nessage: %s'%(message[1]))
                self.do_work(message[1], browser)
            except Exception:
                import traceback
                util.write_log_error(self.lock, self.logger,"list_page_handler process catched exception." + traceback.print_exc())

    def launch(self):
        while len(self.phantomjs_webdrivers)<config.MAX_LIST_PAGE_HANDLER_PROCESS_NUM:
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
        logger = util.initLog(config.LOGGER_NAME_LIST_PAGE_HANDLER)
    multiprocessing.current_process().name = 'list_page_handler_process_main'
    list_page_handler = List_page_handler(logger = logger, host = config.REDIS_HOST, port = config.REDIS_PORT)
    util.write_log_info(list_page_handler.lock, list_page_handler.logger,"[+]start list_page_handler...")
    list_page_handler.launch()
    try:
        content=raw_input()
        while content != 'exit':
            content=raw_input()
    except KeyboardInterrupt:
        pass
    util.write_log_info(list_page_handler.lock, list_page_handler.logger,"user determined list_page_handler")
    list_page_handler.quit()

if __name__ == '__main__':
    main(sys.argv)