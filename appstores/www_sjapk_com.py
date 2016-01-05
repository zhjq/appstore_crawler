# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.sjapk.com"
    START_URLS=["http://www.sjapk.com/T-1-8-1-1.html","http://www.sjapk.com/T-1-9-1-1.html","http://www.sjapk.com/T-1-10-1-1.html","http://www.sjapk.com/T-1-12-1-1.html","http://www.sjapk.com/T-1-11-1-1.html","http://www.sjapk.com/T-1-7-1-1.html","http://www.sjapk.com/T-1-4-1-1.html","http://www.sjapk.com/T-1-2-1-1.html","http://www.sjapk.com/T-1-6-1-1.html","http://www.sjapk.com/T-1-3-1-1.html","http://www.sjapk.com/T-1-1-1-1.html","http://www.sjapk.com/T-1-5-1-1.html","http://www.sjapk.com/T-2-27-1-1.html","http://www.sjapk.com/T-2-14-1-1.html","http://www.sjapk.com/T-2-52-1-1.html","http://www.sjapk.com/T-2-53-1-1.html","http://www.sjapk.com/T-2-25-1-1.html","http://www.sjapk.com/T-2-15-1-1.html","http://www.sjapk.com/T-2-24-1-1.html","http://www.sjapk.com/T-2-16-1-1.html","http://www.sjapk.com/T-2-18-1-1.html","http://www.sjapk.com/T-2-13-1-1.html","http://www.sjapk.com/T-2-17-1-1.html","http://www.sjapk.com/T-2-54-1-1.html","http://www.sjapk.com/T-2-55-1-1.html","http://www.sjapk.com/T-2-56-1-1.html","http://www.sjapk.com/T-2-22-1-1.html","http://www.sjapk.com/T-2-26-1-1.html","http://www.sjapk.com/T-2-20-1-1.html","http://www.sjapk.com/T-2-58-1-1.html","http://www.sjapk.com/T-2-23-1-1.html","http://www.sjapk.com/T-2-57-1-1.html","http://www.sjapk.com/T-2-19-1-1.html","http://www.sjapk.com/T-2-21-1-1.html","http://www.sjapk.com/T-5-12-1-1.html"]
    DETAIL_URLS="//div[@class='main_down']/ul/li/span/h1/a"
    DOWNLOAD_URL="//div[@class='main_r_xiazai5']/a[1]"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='main_r_f']/h1"
    CATEGORY="//div[@class='suozaidi']/a[2]"
    RATING="//div[@class='main_r_xiazai3']/div[2]/font"
    UPLOAD_TIME="//div[@class='main_r_xiazai3']/div[1]/p/font[2]"

    def get_upload_time(self,detail_page_driver):
        if self.UPLOAD_TIME is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.UPLOAD_TIME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            upload_time = util.unify_data(ele.text.split(" ")[0])
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
            rating = str(float(ele.text.split(" ")[1].split("分")[0])*10)
        except Exception as e:
            return None
        return rating
