# -*- coding: utf-8 -*-
import threading
import time
import logging
import multiprocessing

HIGH_DOWNLOAD_QUEUE = 'high_download_queue'
LOW_DOWNLOAD_QUEUE = 'low_download_queue'
HIGH_FILE_HANDLE_QUEUE = 'high_file_handle_queue'
LOW_FILE_HANDLE_QUEUE = 'low_file_handle_queue'
HIGH_DETAIL_PAGE_HANDLE_QUEUE = 'high_detail_page_handle_queue'
LOW_DETAIL_PAGE_HANDLE_QUEUE = 'low_detail_page_handle_queue'
HIGH_LIST_PAGE_HANDLE_QUEUE = 'high_list_page_handle_queue'
LOW_LIST_PAGE_HANDLE_QUEUE = 'low_list_page_handle_queue'

'''
关于爬取或下载时的user-agent设置，
一般来说准备多个user-agent，爬取时从里面进行随即挑选以模仿用户访问行为。
但实际发现有个别网站需要特定的user-agent才能访问，目前phantomjs无法判断网页没有返回希望的结果
（在此通常指在页面中找到希望的元素，例如下载链接，详情页链接等）
是否是因为user-agent的原因，所以也不方便采取网页没有返回希望的结果就更换user-agent的策略。
所以此处暂时采取给定一个普遍通用的user-agent，特殊站点可以传递特定user-agent参数的做法。
未来也许会在个别网站特定user-agent和随机user-agent中做衡量取舍。
'''
REQUEST_HEADERS = {'User-Agent': 'AndroidDownloadManager/4.1.1 (Linux; U; Android 4.1.1; Nexus S Build/JRO03E)'}
PHANTOMJS_USER_AGENT = ("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0")

REQUESTS_ACTION_GET = 'GET'
REQUESTS_ACTION_POST = 'POST'

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

SOCKET_TIMEOUT = 10
REQUESTS_TIMEOUT = 5

'''
将爬取过的detail_page_url和list_page_url的md5值存到redis的db11和db10中，
并设置的过期时间，以使在这段时间内不会被重复爬取，此处为1天
'''
CRAWLED_URL_REDIS_TIMEOUT = 86400

MAX_DOWNLOAD_THREAD_NUM = 7
MAX_FILEHANDLE_PROCESS_NUM = multiprocessing.cpu_count()/2
MAX_DETAIL_PAGE_HANDLER_PROCESS_NUM = multiprocessing.cpu_count()/2
MAX_LIST_PAGE_HANDLER_PROCESS_NUM = multiprocessing.cpu_count()/2

DEFAULT_DOWNLOAD_FOLDER = 'download_folder/tmp/'
DEFAULT_FILE_HANDLE_FOLDER = 'download_folder/'
DEFAULT_DOWNLOAD_FILE_TYPE = 'apk'

FILE_TYPE = {
    'apk':{
        'extension_filename':'.apk',
        'content-type':[
            'application/vnd.android',
            'application/vnd.android.package-archive',
            'application/octet-stream',
            'application/x-www-form-urlencoded',
            'text/plain',
            'apk'
        ]
    }
}

#webdriver页面加载超时时间
PAGE_LOAD_TIMEOUT = 4
#webdriver元素查找超时时间
IMPLICITLY_WAIT_TIME = 2
SCRIPT_TIMEOUT = 5

LOGGER_ENABLED = True
LOGGER_NAME_DETAIL_PAGE_HANDLER = 'detail_page_handler.log'
LOGGER_NAME_LIST_PAGE_HANDLER = 'list_page_handler.log'
LOGGER_NAME_DOWNLOADER = 'downloader.log'
LOGGER_NAME_FILE_HANDLER = 'file_handler.log'
LOGGER_LEVEL = logging.DEBUG
FILE_LOGGER_LEVEL = logging.DEBUG
CONSOLE_LOGGER_LEVEL = logging.DEBUG
LOGGER_FORMATTER = "%(asctime)s %(levelname)s %(message)s"

MESSAGE_TYPE_NORMAL = 'normal'
MESSAGE_TYPE_CRAWL = 'crawl'
