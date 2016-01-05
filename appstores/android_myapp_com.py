# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="android.myapp.com"
    START_URLS=["http://android.myapp.com/myapp/category.htm?orgame=2&categoryId=147","http://android.myapp.com/myapp/category.htm?orgame=2&categoryId=121","http://android.myapp.com/myapp/category.htm?orgame=2&categoryId=144","http://android.myapp.com/myapp/category.htm?orgame=2&categoryId=148","http://android.myapp.com/myapp/category.htm?orgame=2&categoryId=149","http://android.myapp.com/myapp/category.htm?orgame=2&categoryId=153","http://android.myapp.com/myapp/category.htm?orgame=2&categoryId=146","http://android.myapp.com/myapp/category.htm?orgame=2&categoryId=151","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=103","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=101","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=122","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=102","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=112","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=106","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=104","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=110","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=115","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=119","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=111","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=107","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=118","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=108","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=100","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=114","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=117","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=109","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=105","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=113","http://android.myapp.com/myapp/category.htm?orgame=1&categoryId=116"]
    DETAIL_URLS="//ul[@class='app-list clearfix']/li/div[@class='app-info clearfix']/div[@class='app-info-desc']/a[@class='name ofh']"
    DOWNLOAD_URL="//a[@class='det-down-btn']"
    SCROLL_DOWN=7
    CHECKMORE="//a[text()='加载更多']"
    APPNAME="//div[@class='det-name-int']"
    UPLOAD_TIME="//div[@id='J_ApkPublishTime']"
    DOWNLOAD_COUNT="//div[@class='det-ins-num']"
    RATING="//div[@class='com-blue-star-num']"
    CATEGORY="//a[@id='J_DetCate']"

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.text.split("分")[0])*20)
        except Exception as e:
            return None
        return rating

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
        return ele.get_attribute("data-apkurl")
