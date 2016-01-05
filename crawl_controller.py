import redis
import json

import sys
sys.path.append("appstores")

import appstore_list

import config

def push_message(rd, out_json_message):
    next_queue = out_json_message['next_queue']
    del out_json_message['next_queue']
    return rd.lpush(next_queue, json.dumps(out_json_message))

rd = redis.Redis()
######################################################
for appstore in appstore_list.appstores:
    appstore_modual = __import__(appstore)
    appstore_class = appstore_modual.Store()
    list_page_urls = appstore_class.get_list_page_urls()
    detail_page_urls = appstore_class.get_detail_page_urls()
    source = appstore_class.SOURCE
    for list_page_url in list_page_urls:
        out_json_message = {}
        out_json_message['source'] = appstore
        out_json_message['list_page_url'] = list_page_url
        out_json_message['message_type'] = config.MESSAGE_TYPE_CRAWL
        out_json_message['next_queue'] = config.LOW_LIST_PAGE_HANDLE_QUEUE
        print out_json_message
        push_message(rd, out_json_message)
    for detail_page_url in detail_page_urls:
        out_json_message = {}
        out_json_message['source'] = appstore
        out_json_message['detail_page_url'] = detail_page_url
        out_json_message['message_type'] = config.MESSAGE_TYPE_CRAWL
        out_json_message['next_queue'] = config.LOW_DETAIL_PAGE_HANDLE_QUEUE
        print out_json_message
        push_message(rd, out_json_message)

