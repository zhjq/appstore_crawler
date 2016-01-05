# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="app.sogou.com"
    START_URLS=["http://app.sogou.com/game","http://app.sogou.com/soft"]
    DETAIL_URLS="//div[@class='list_inner']/ul[@class='cf']/li/dl[@class='cf']/dd/h3/a"
    DOWNLOAD_URL="//div[@class='down_pc cf']/a[@class='down_pc_btn']"
    NEXTPAGE="//a[text()='>']"
    APPNAME="//div[@class='d-title cf']/em"
    CATEGORY="//div[@class='sub_nav cf']/a[3]"
    DOWNLOAD_COUNT="//ul[@class='dd cf']/li[1]"
    UPLOAD_TIME="//ul[@class='dd cf']/li[2]"
    RATING="//div[@class='star']/div[@class='star_min']/em"


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
