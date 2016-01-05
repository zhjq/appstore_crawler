# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="app.mi.com"
    START_URLS=["http://app.mi.com/category/5","http://app.mi.com/category/27","http://app.mi.com/category/2","http://app.mi.com/category/7","http://app.mi.com/category/12","http://app.mi.com/category/10","http://app.mi.com/category/9","http://app.mi.com/category/4","http://app.mi.com/category/3","http://app.mi.com/category/6","http://app.mi.com/category/14","http://app.mi.com/category/8","http://app.mi.com/category/11","http://app.mi.com/category/13","http://app.mi.com/category/1","http://app.mi.com/category/16","http://app.mi.com/category/17","http://app.mi.com/category/18","http://app.mi.com/category/19","http://app.mi.com/category/20","http://app.mi.com/category/21","http://app.mi.com/category/22","http://app.mi.com/category/23","http://app.mi.com/category/25","http://app.mi.com/category/26","http://app.mi.com/category/28","http://app.mi.com/category/29"]
    DETAIL_URLS="//ul[@id='all-applist']/li/h5/a"
    DOWNLOAD_URL="//a[@class='download']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='intro-titles']/h3"
    CATEGORY="//div[@class='bread-crumb']/ul/li[2]/a"
    RATING="//div[@class='star1-empty']/div"
    UPLOAD_TIME="//div[@class='details preventDefault']/ul/li[6]"

    def get_upload_time(self,detail_page_driver):
        if self.UPLOAD_TIME is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.UPLOAD_TIME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            upload_time = util.unify_data(ele.get_attribute("textContent").strip())
        except Exception as e:
            return None
        return upload_time

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("class").split('star1-hover star1-')[1])*10)
        except Exception as e:
            return None
        return rating
