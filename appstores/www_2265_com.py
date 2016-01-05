# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.2265.com"
    START_URLS=["http://www.2265.com/game_1/","http://www.2265.com/soft_8/","http://www.2265.com/game_2/","http://www.2265.com/soft_9/","http://www.2265.com/game_3/","http://www.2265.com/soft_10/","http://www.2265.com/game_4/","http://www.2265.com/soft_11/","http://www.2265.com/game_5/","http://www.2265.com/soft_12/","http://www.2265.com/game_6/","http://www.2265.com/soft_13/","http://www.2265.com/game_7/","http://www.2265.com/soft_14/","http://www.2265.com/soft_15/","http://www.2265.com/soft_16/"]
    DETAIL_URLS="//div[@id='listboxsix']/ul/li/div/div/dl/dt/a"
    DOWNLOAD_URL="//a[text()='官方正版']|//a[text()='本地下载']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='right']/div[@class='proinfo']/h1"
    UPLOAD_TIME="//div[@class='detinfo']/div[@class='left']/p[3]"
    DOWNLOAD_COUNT="//div[@class='detinfo']/div[@class='left']/p[1]"
    RATING="//span[@class='vote-column-s']/i"
    CATEGORY="//div[@class='mapnav']/a[3]"

    def get_upload_time(self,detail_page_driver):
        if self.UPLOAD_TIME is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.UPLOAD_TIME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            upload_time = util.unify_data(ele.text.split("时间：")[1])
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

