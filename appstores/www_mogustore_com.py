# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.mogustore.com"
    START_URLS=["http://www.mogustore.com/app_110.html","http://www.mogustore.com/app_111.html","http://www.mogustore.com/app_112.html","http://www.mogustore.com/app_113.html","http://www.mogustore.com/app_114.html","http://www.mogustore.com/app_115.html","http://www.mogustore.com/app_117.html","http://www.mogustore.com/app_118.html","http://www.mogustore.com/app_120.html","http://www.mogustore.com/app_121.html","http://www.mogustore.com/app_122.html","http://www.mogustore.com/app_123.html","http://www.mogustore.com/app_124.html","http://www.mogustore.com/app_125.html","http://www.mogustore.com/app_126.html","http://www.mogustore.com/app_127.html","http://www.mogustore.com/app_128.html","http://www.mogustore.com/app_129.html","http://www.mogustore.com/app_130.html","http://www.mogustore.com/game_210.html","http://www.mogustore.com/game_211.html","http://www.mogustore.com/game_212.html","http://www.mogustore.com/game_213.html","http://www.mogustore.com/game_214.html","http://www.mogustore.com/game_215.html","http://www.mogustore.com/game_216.html","http://www.mogustore.com/game_217.html","http://www.mogustore.com/game_218.html","http://www.mogustore.com/game_219.html","http://www.mogustore.com/game_220.html","http://www.mogustore.com/game_221.html","http://www.mogustore.com/game_222.html"]
    DETAIL_URLS="//div[@class='title']/h2/a"
    DOWNLOAD_URL="//li[@class='l down']/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='sub_title']/h1"
    CATEGORY="//div[@class='services_title']/h2/a[3]"
    DOWNLOAD_COUNT="//div[@class='sub_title']/ul/li[6]"
    UPLOAD_TIME="//div[@class='sub_title']/ul/li[5]"
    RATING="//div[@class='sub_title']/ul/li[2]/img"

    def get_rating(self,detail_page_driver):
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("src").split("/")[-1].split('.')[0])*10)
        except Exception as e:
            return None
        return rating