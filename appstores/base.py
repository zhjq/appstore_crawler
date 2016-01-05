# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("..")

from selenium import webdriver
import selenium.common.exceptions as selenium_exception
import time
import config
import util

class Base(object):
    PHANTOMJS_USER_AGENT = ("Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0")
    REQ_HEADER = {'User-Agent': 'AndroidDownloadManager/4.1.1 (Linux; U; Android 4.1.1; Nexus S Build/JRO03E)'}
    REQ_COOKIE = None
    SOURCE = None
    START_URLS = []
    DETAIL_URLS = None
    DOWNLOAD_URL = None
    NEXTPAGE = None
    CHECKMORE = None
    SCROLL_DOWN = 0
    APPNAME = None
    CATEGORY = None
    RATING = None
    DOWNLOAD_COUNT = None
    UPLOAD_TIME = None
    OTHERINFO = None

    def scroll_down(self, list_page_driver):
        if self.SCROLL_DOWN == 0:
            return
        js = "var q = document.documentElement.scrollTop = 10000"
        for i in xrange(self.SCROLL_DOWN):
            list_page_driver.execute_script(js)
            time.sleep(1.5)
        return

    def click_checkmore(self, list_page_driver):
        if self.CHECKMORE is None:
            return 0
        count = 0
        while True:
            try:
                ele = list_page_driver.find_element_by_xpath(self.CHECKMORE)
            except selenium_exception.NoSuchElementException as e:
                break
            try:
                ele.click()
            except selenium_exception.ElementNotVisibleException as e:
                break
            time.sleep(1.5)
            count += 1
        return count

    def get_detail_urls(self, list_page_driver):
        detail_urls = []
        eles = list_page_driver.find_elements_by_xpath(self.DETAIL_URLS)
        if len(eles) == 0:
            try:
                list_page_driver.refresh()
            except selenium_exception.TimeoutException as e:
                pass
            eles = list_page_driver.find_elements_by_xpath(self.DETAIL_URLS)
        for ele in eles:
            detail_url = util.href2url(self.SOURCE, ele.get_attribute('href'), util.get_current_url(list_page_driver))
            if detail_url:
                detail_urls.append(detail_url)
        return detail_urls

    def get_download_url(self, detail_page_driver):
        download_url = None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_URL)
        except selenium_exception.NoSuchElementException as e:
            try:
                detail_page_driver.refresh()
            except selenium_exception.TimeoutException as e:
                pass
            try:
                ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_URL)
            except selenium_exception.NoSuchElementException as e:
                return download_url
        return util.href2url(self.SOURCE, ele.get_attribute('href'), util.get_current_url(detail_page_driver))

    def get_appname(self, detail_page_driver):
        if self.APPNAME is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.APPNAME)
        except selenium_exception.NoSuchElementException as e:
            return None
        return ele.text.strip()

    def get_category(self, detail_page_driver):
        if self.CATEGORY is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.CATEGORY)
        except selenium_exception.NoSuchElementException as e:
            return None
        return ele.text.replace("类别", "").replace("所属", "").replace(" ", "").replace("\r", "").replace("\n", "").replace(":", "").replace("：", "").strip()

    def get_rating(self, detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        return ele.text.strip()

    def get_download_count(self, detail_page_driver):
        if self.DOWNLOAD_COUNT is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_COUNT)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            download_count = util.unify_download_count(ele.text.strip())
        except Exception as e:
            return None
        return download_count

    def get_upload_time(self, detail_page_driver):
        if self.UPLOAD_TIME is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.UPLOAD_TIME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            upload_time = util.unify_data(ele.text.strip())
        except Exception as e:
            return None
        return upload_time

    def get_otherinfo(self, detail_page_driver):
        if self.OTHERINFO is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.OTHERINFO)
        except selenium_exception.NoSuchElementException as e:
            return None
        return ele.text.strip()    

    def click_nextpage(self, list_page_driver):
        if self.NEXTPAGE is None:
            return None
        try:
            ele = list_page_driver.find_element_by_xpath(self.NEXTPAGE)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            ele.click()
        except selenium_exception.TimeoutException as e:
            pass
        time.sleep(1.5)
        return util.get_current_url(list_page_driver)

    def get_list_page_urls(self):
        return self.START_URLS

    def get_detail_page_urls(self):
        return []
    def get_download_method(self):
        return config.REQUESTS_ACTION_GET
    def get_download_data(self):
        return None
    def get_download_cookie_producer(self):
        return None

    def make_detail2download_json_message(self, browser):
        out_json_message={}
        out_json_message['source'] = self.SOURCE
        out_json_message['request_headers'] = self.REQ_HEADER
        out_json_message['method'] = self.get_download_method()
        out_json_message['data'] = self.get_download_data()
        out_json_message['download_cookie_producer'] = self.get_download_cookie_producer()
        app_name = self.get_appname(browser)
        category = self.get_category(browser)
        rating = self.get_rating(browser)
        download_count = self.get_download_count(browser)
        upload_time = self.get_upload_time(browser)
        otherinfo = self.get_otherinfo(browser)
        if app_name is not None:
            out_json_message['app_name']=app_name
        if category is not None:
            out_json_message['category']=category
        if rating is not None:
            out_json_message['rating']=rating
        if download_count is not None:
            out_json_message['download_count']=download_count
        if upload_time is not None:
            out_json_message['upload_time']=upload_time
        if otherinfo is not None:
            out_json_message['otherinfo']=otherinfo
        return out_json_message



















            
