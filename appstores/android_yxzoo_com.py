# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="android.yxzoo.com"
    START_URLS=["http://android.yxzoo.com/soft","http://android.yxzoo.com/game/lx_3","http://android.yxzoo.com/game/lx_4","http://android.yxzoo.com/game/lx_5","http://android.yxzoo.com/game/lx_6","http://android.yxzoo.com/game/lx_7","http://android.yxzoo.com/game/lx_8","http://android.yxzoo.com/game/lx_9","http://android.yxzoo.com/game/lx_10","http://android.yxzoo.com/game/lx_1","http://android.yxzoo.com/game/lx_2"] 
    DETAIL_URLS="//div[@id='list2']/dl/dt/a"
    DOWNLOAD_URL="//div[@class='downlist']/a[@id='download_pc']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='cmain2']/div[1]/div[1]/h1"
    CATEGORY="//div[@class='info_r']/ul/li[1]"
    UPLOAD_TIME="//div[@class='info_r']/ul/li[last()]"
    RATING="//span[@class='level_big']/i"

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

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("style").split(":")[1].split("%")[0]))
        except Exception as e:
            return None
        return rating

