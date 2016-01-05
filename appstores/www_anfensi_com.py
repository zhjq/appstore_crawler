# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.anfensi.com"
    START_URLS=["http://www.anfensi.com/soft/49_1_1.html","http://www.anfensi.com/game/0_3_0_1_1.html","http://www.anfensi.com/soft/50_1_1.html","http://www.anfensi.com/game/0_4_0_1_1.html","http://www.anfensi.com/soft/51_1_1.html","http://www.anfensi.com/game/0_5_0_1_1.html","http://www.anfensi.com/soft/52_1_1.html","http://www.anfensi.com/game/0_6_0_1_1.html","http://www.anfensi.com/soft/53_1_1.html","http://www.anfensi.com/game/0_7_0_1_1.html","http://www.anfensi.com/soft/54_1_1.html","http://www.anfensi.com/game/0_8_0_1_1.html","http://www.anfensi.com/soft/55_1_1.html","http://www.anfensi.com/game/0_9_0_1_1.html","http://www.anfensi.com/soft/56_1_1.html","http://www.anfensi.com/game/0_10_0_1_1.html","http://www.anfensi.com/soft/57_1_1.html","http://www.anfensi.com/game/0_11_0_1_1.html","http://www.anfensi.com/soft/58_1_1.html","http://www.anfensi.com/game/0_12_0_1_1.html","http://www.anfensi.com/soft/59_1_1.html","http://www.anfensi.com/game/0_13_0_1_1.html","http://www.anfensi.com/soft/60_1_1.html","http://www.anfensi.com/soft/61_1_1.html","http://www.anfensi.com/soft/62_1_1.html","http://www.anfensi.com/soft/63_1_1.html","http://www.anfensi.com/soft/64_1_1.html","http://www.anfensi.com/soft/65_1_1.html","http://www.anfensi.com/game/0_14_0_1_1.html","http://www.anfensi.com/soft/66_1_1.html","http://www.anfensi.com/soft/67_1_1.html","http://www.anfensi.com/soft/68_1_1.html","http://www.anfensi.com/game/0_15_0_1_1.html"]
    DETAIL_URLS="//div[@class='sxjg']/ul/li/div/p/a[@target='_blank']"
    DOWNLOAD_URL="//p[@id='game-down']/b/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//p[@id='main-title']"
    CATEGORY="//p[@class='info']/b[1]"
    UPLOAD_TIME="//p[@class='info']/b[6]"

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

    def get_appname(self,detail_page_driver):
        if self.APPNAME is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.APPNAME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            appname = ele.text.split(">")[2].strip()
        except Exception as e:
            return None
        return appname
