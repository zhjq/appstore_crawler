# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.9553.com"
    START_URLS=["http://www.9553.com/android/258_1.htm","http://www.9553.com/android/270_1.htm","http://www.9553.com/android/240_1.htm","http://www.9553.com/android/238_1.htm","http://www.9553.com/android/239_1.htm","http://www.9553.com/android/254_1.htm","http://www.9553.com/android/255_1.htm","http://www.9553.com/android/256_1.htm","http://www.9553.com/android/257_1.htm","http://www.9553.com/android/259_1.htm","http://www.9553.com/android/260_1.htm","http://www.9553.com/android/264_1.htm","http://www.9553.com/android/261_1.htm","http://www.9553.com/android/263_1.htm","http://www.9553.com/android/235_1.htm","http://www.9553.com/android/245_1.htm","http://www.9553.com/android/244_1.htm","http://www.9553.com/android/249_1.htm","http://www.9553.com/android/242_1.htm","http://www.9553.com/android/243_1.htm","http://www.9553.com/android/252_1.htm","http://www.9553.com/android/247_1.htm","http://www.9553.com/android/248_1.htm","http://www.9553.com/android/250_1.htm","http://www.9553.com/android/253_1.htm","http://www.9553.com/android/251_1.htm"] 
    DETAIL_URLS="//ul[@class='mod-img-list soft_hover android_down']/li/p[1]/b/a"
    DOWNLOAD_URL="//div[@class='fl_lf soft_details_btn']/ul/li[1]/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='fl_lf soft_info']/h1"
    CATEGORY="//div[@class='fl_lf soft_info']/ul/li[3]"
    UPLOAD_TIME="//div[@class='fl_lf soft_info']/ul/li[4]"
    DOWNLOAD_COUNT="//div[@class='fl_lf soft_info']/ul/li[2]"
    RATING="//em[@id='score']"

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
            download_count = util.unify_download_count(ele.text.split("人气：")[1])
        except Exception as e:
            return None
        return download_count

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.text)*10)
        except Exception as e:
            return None
        return rating
