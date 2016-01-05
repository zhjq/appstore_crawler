# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.9game.cn"
    START_URLS=["http://www.9game.cn/category/2_0_97_0_0_1/","http://www.9game.cn/category/2_0_52_0_0_1/","http://www.9game.cn/category/2_0_94_0_0_1/","http://www.9game.cn/category/2_7_0_0_0_1/","http://www.9game.cn/category/2_0_39_0_0_1/","http://www.9game.cn/category/2_0_108_0_0_1/","http://www.9game.cn/category/2_0_14_0_0_1/","http://www.9game.cn/category/2_4_0_0_0_1/","http://www.9game.cn/category/2_0_75_0_0_1/","http://www.9game.cn/category/2_0_38_0_0_1/","http://www.9game.cn/category/2_0_31_0_0_1/","http://www.9game.cn/category/2_0_92_0_0_1/"]
    DETAIL_URLS="//div[@class='game-poker-con']/ul/li/a[1]"
    DOWNLOAD_URL="//div[@class='android-detail down-con']/a"
    SCROLL_DOWN=3
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//h1[@class='h1-title']/a | div[@class='h1-title']/h1"
    CATEGORY="//div[@class='p-des']/p[1]"
    RATING="//div[@class='left']/div[@class='big-s']"

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
            category = ele.text.split(":")[1].split("评论")[0]
            category = category.replace(" ","")
        except Exception as e:
            return None
        return category
