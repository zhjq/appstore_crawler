# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="d.gao7.com"
    START_URLS=["http://d.gao7.com/app/2-0-0-0-29-all-0-1","http://d.gao7.com/app/2-0-0-0-33-all-0-1","http://d.gao7.com/app/2-0-1-0-34-yuedujiaoyu-1012292-1","http://d.gao7.com/app/2-0-0-0-35-all-0-1","http://d.gao7.com/app/2-0-0-0-36-all-0-1","http://d.gao7.com/app/2-0-0-0-37-all-0-1","http://d.gao7.com/app/2-0-0-0-38-all-0-1","http://d.gao7.com/app/2-0-0-0-39-all-0-1","http://d.gao7.com/app/2-0-0-0-40-all-0-1","http://d.gao7.com/app/2-0-0-0-32-all-0-1","http://d.gao7.com/app/2-0-0-0-31-all-0-1","http://d.gao7.com/app/2-0-0-0-30-all-0-1","http://d.gao7.com/game/2-1-1-3-102-%E5%86%85%E8%B4%AD%E7%A0%B4%E8%A7%A3-0-1","http://d.gao7.com/game/2-0-0-0-20-all-0-1","http://d.gao7.com/game/2-0-0-0-22-all-0-1","http://d.gao7.com/game/2-0-0-0-23-all-0-1","http://d.gao7.com/game/2-0-0-0-24-all-0-1","http://d.gao7.com/game/2-0-0-0-25-all-0-1","http://d.gao7.com/game/2-0-0-0-26-all-0-1","http://d.gao7.com/game/2-0-0-0-27-all-0-1","http://d.gao7.com/game/2-0-0-0-28-all-0-1"]
    DETAIL_URLS="//ul[@class='fix']/li/div[2]/h3/a"
    DOWNLOAD_URL="//div[@class='mod mod-app-d app-d-android app-d-cur']/div[2]/dl/dd[2]/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='mod mod-app-meta']/dl/dd/h2"
    CATEGORY="//div[@class='mod mod-app-meta']/dl/dd/p[2]/span[1]"
    UPLOAD_TIME="//div[@class='mod mod-app-meta']/dl/dd/p[3]/span[2]/strong/time"
    RATING="//p[@class='app-meta-rate fix']/strong"

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
            category = ele.text.split("：")[1]
        except Exception as e:
            return None
        return category
