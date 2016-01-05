# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="wy.155.cn"
    START_URLS=["http://android.155.cn/netgame/"]
    DETAIL_URLS="//div[@class='on_cent_left list_dl3']/dl/dt/a"
    DOWNLOAD_URL="//a[@class='down']"
    NEXTPAGE="//a[text()='下页']"
    APPNAME="//div[@class='cent1_left']/h1"
    CATEGORY="//ul[@class='c1_ul']/li[1]"
    UPLOAD_TIME="//ul[@class='c1_ul']/li[6]"
    DOWNLOAD_COUNT="//ul[@class='c1_ul']/li[5]"

    def get_upload_time(self,detail_page_driver):
        if self.UPLOAD_TIME is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.UPLOAD_TIME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            upload_time = util.unify_data(ele.text.split("更新：")[1].split(" ")[0])
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
            download_count = util.unify_download_count(ele.text.split("下载：")[1])
        except Exception as e:
            return None
        return download_count

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
