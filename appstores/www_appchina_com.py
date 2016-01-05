# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.appchina.com"
    START_URLS=["http://www.appchina.com/category/301.html","http://www.appchina.com/category/302.html","http://www.appchina.com/category/303.html","http://www.appchina.com/category/304.html","http://www.appchina.com/category/305.html","http://www.appchina.com/category/306.html","http://www.appchina.com/category/307.html","http://www.appchina.com/category/308.html","http://www.appchina.com/category/309.html","http://www.appchina.com/category/310.html","http://www.appchina.com/category/311.html","http://www.appchina.com/category/312.html","http://www.appchina.com/category/313.html","http://www.appchina.com/category/314.html","http://www.appchina.com/category/315.html","http://www.appchina.com/category/411.html","http://www.appchina.com/category/412.html","http://www.appchina.com/category/413.html","http://www.appchina.com/category/414.html","http://www.appchina.com/category/415.html","http://www.appchina.com/category/416.html","http://www.appchina.com/category/417.html","http://www.appchina.com/category/418.html","http://www.appchina.com/category/419.html","http://www.appchina.com/category/420.html","http://www.appchina.com/category/421.html","http://www.appchina.com/category/422.html","http://www.appchina.com/category/423.html","http://www.appchina.com/category/424.html"]
    DETAIL_URLS="//div[@class='app-info']/h1[@class='app-name']/a"
    DOWNLOAD_URL="//div[@class='download-button direct_download']/a"
    NEXTPAGE="//a[@class='next']"
    APPNAME="//h1[@class='app-name']"
    CATEGORY="//div[@class='breadcrumb centre-content']/a[3]"
    UPLOAD_TIME="//span[@class='app-statistic']"
    DOWNLOAD_COUNT="//span[@class='app-statistic']"

    def get_upload_time(self,detail_page_driver):
        if self.UPLOAD_TIME is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.UPLOAD_TIME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            upload_time = util.unify_data(ele.text.split("更新：")[1])
        except Exception as e:
            return None
        return upload_time

    def get_download_count(self,detail_page_driver):
        if self.DOWNLOAD_COUNT is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_COUNT)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            download_count = util.unify_download_count(ele.text.split("下载")[0])
        except Exception as e:
            return None
        return download_count
