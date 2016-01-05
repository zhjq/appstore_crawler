# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.9ht.com"
    START_URLS=["http://www.9ht.com/pc/148_1.html","http://www.9ht.com/pc/145_1.html","http://www.9ht.com/pc/144_1.html","http://www.9ht.com/pc/146_1.html","http://www.9ht.com/pc/143_1.html","http://www.9ht.com/pc/147_1.html","http://www.9ht.com/pc/149_1.html","http://www.9ht.com/pc/150_1.html","http://www.9ht.com/pc/151_1.html","http://www.9ht.com/pc/152_1.html","http://www.9ht.com/pc/153_1.html","http://www.9ht.com/pc/155_1.html","http://www.9ht.com/pc/156_1.html","http://www.9ht.com/pc/157_1.html","http://www.9ht.com/pc/158_1.html","http://www.9ht.com/pc/159_1.html","http://www.9ht.com/pc/252_1.html","http://www.9ht.com/pc/256_1.html","http://www.9ht.com/pc/207_1.html","http://www.9ht.com/pc/208_1.html","http://www.9ht.com/pc/209_1.html","http://www.9ht.com/pc/210_1.html","http://www.9ht.com/pc/211_1.html","http://www.9ht.com/pc/212_1.html","http://www.9ht.com/pc/213_1.html","http://www.9ht.com/pc/214_1.html","http://www.9ht.com/pc/215_1.html","http://www.9ht.com/pc/243_1.html","http://www.9ht.com/pc/244_1.html","http://www.9ht.com/pc/245_1.html","http://www.9ht.com/pc/246_1.html","http://www.9ht.com/pc/247_1.html","http://www.9ht.com/pc/248_1.html","http://www.9ht.com/pc/249_1.html","http://www.9ht.com/pc/250_1.html","http://www.9ht.com/pc/251_1.html"]
    DETAIL_URLS="//dd[@id='lcont']/ul/li/b/a"
    DOWNLOAD_URL="//ul[@class='ul_Address']/li[last()]/a"
    NEXTPAGE="//a[@class='tsp_next']"
    APPNAME="//dd[@id='linfo']/h1"
    CATEGORY="//dd[@id='linfo']/p[last()]/i[2]"
    UPLOAD_TIME="//dd[@id='linfo']/p[last()]/i[3]"
    RATING="//dd[@id='linfo']/p[last()]/i[1]/span"

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("class").split("star")[1])*20)
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
            category = ele.text.split("：")[1]
        except Exception as e:
            return None
        return category