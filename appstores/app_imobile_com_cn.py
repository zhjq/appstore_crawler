# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="app.imobile.com.cn"
    START_URLS=["http://app.imobile.com.cn/android/soft/3/hot.html","http://app.imobile.com.cn/android/soft/4/hot.html","http://app.imobile.com.cn/android/game/22/hot.html","http://app.imobile.com.cn/android/soft/5/hot.html","http://app.imobile.com.cn/android/soft/6/hot.html","http://app.imobile.com.cn/android/game/23/hot.html","http://app.imobile.com.cn/android/soft/7/hot.html","http://app.imobile.com.cn/android/soft/8/hot.html","http://app.imobile.com.cn/android/game/24/hot.html","http://app.imobile.com.cn/android/soft/9/hot.html","http://app.imobile.com.cn/android/soft/10/hot.html","http://app.imobile.com.cn/android/game/25/hot.html","http://app.imobile.com.cn/android/soft/11/hot.html","http://app.imobile.com.cn/android/soft/12/hot.html","http://app.imobile.com.cn/android/game/26/hot.html","http://app.imobile.com.cn/android/soft/13/hot.html","http://app.imobile.com.cn/android/soft/14/hot.html","http://app.imobile.com.cn/android/game/27/hot.html","http://app.imobile.com.cn/android/soft/15/hot.html","http://app.imobile.com.cn/android/soft/16/hot.html","http://app.imobile.com.cn/android/game/28/hot.html","http://app.imobile.com.cn/android/soft/17/hot.html","http://app.imobile.com.cn/android/soft/18/hot.html","http://app.imobile.com.cn/android/game/29/hot.html","http://app.imobile.com.cn/android/soft/19/hot.html","http://app.imobile.com.cn/android/soft/20/hot.html","http://app.imobile.com.cn/android/game/30/hot.html"]
    DETAIL_URLS="//div[@class='main']/ul/li/div[1]/h3/a"
    DOWNLOAD_URL="//div[@class='download_install']/a[@class='download']"
    NEXTPAGE="//a[text()='>']"
    APPNAME="//div[@class='box700_intro']/h1"
    CATEGORY="//ul[@class='app_params']/li[2]"
    UPLOAD_TIME="//ul[@class='app_params']/li[3]"
    DOWNLOAD_COUNT="//ul[@class='app_params']/li[5]"
    RATING="//span[@class='score']"

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.text)*20)
        except Exception as e:
            return None
        return rating

    def get_category(self,detail_page_driver):
        if self.CATEGORY is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.CATEGORY)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            category = ele.text.split("/")[1]
            category = category.replace(" ","")
        except Exception as e:
            return None
        return category
