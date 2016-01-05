# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.paojiao.cn"
    START_URLS=["http://www.paojiao.cn/danji/list_default____1.html"]
    DETAIL_URLS="//div[@class='top-list2']/ul/li/a[2]"
    DOWNLOAD_URL="//li[@class='down_li']/a[@class='downbtn1']"
    NEXTPAGE="//a[@class='next']"
    APPNAME="//div[@id='app_base_info']/h2"
    UPLOAD_TIME="//ul[@class='info']/li[5]"
    CATEGORY="//ul[@class='info']/li[4]"
    DOWNLOAD_COUNT="//ul[@class='info']/li[6]"

    def get_category(self,detail_page_driver):
        if self.CATEGORY is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.CATEGORY)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            category = ele.text.split("：")[1]
        except Exception as e:
            return None
        return category

    def get_download_url(self,detail_page_driver):
        download_url = None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_URL)
        except selenium_exception.NoSuchElementException as e:
            detail_page_driver.refresh()
            try:
                ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_URL)
            except selenium_exception.NoSuchElementException as e:
                return download_url
        try:
            download_url = ele.get_attribute("href").split("'")[1]
        except:
            pass
        return download_url
