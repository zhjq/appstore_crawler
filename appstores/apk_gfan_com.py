# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="apk.gfan.com"
    START_URLS=["http://apk.gfan.com/apps_1_1_1.html","http://apk.gfan.com/apps_21_1_1.html","http://apk.gfan.com/apps_2_1_1.html","http://apk.gfan.com/apps_141_1_1.html","http://apk.gfan.com/apps_125_1_1.html","http://apk.gfan.com/apps_3_1_1.html","http://apk.gfan.com/apps_123_1_1.html","http://apk.gfan.com/apps_26_1_1.html","http://apk.gfan.com/apps_124_1_1.html","http://apk.gfan.com/apps_22_1_1.html","http://apk.gfan.com/apps_27_1_1.html","http://apk.gfan.com/apps_122_1_1.html","http://apk.gfan.com/apps_55_1_1.html","http://apk.gfan.com/apps_61_1_1.html","http://apk.gfan.com/apps_49_1_1.html","http://apk.gfan.com/apps_25_1_1.html","http://apk.gfan.com/apps_13_1_1.html","http://apk.gfan.com/apps_6_1_1.html","http://apk.gfan.com/apps_5_1_1.html","http://apk.gfan.com/apps_12_1_1.html","http://apk.gfan.com/apps_11_1_1.html","http://apk.gfan.com/apps_56_1_1.html","http://apk.gfan.com/games_121_1_1.html","http://apk.gfan.com/games_38_1_1.html","http://apk.gfan.com/games_35_1_1.html","http://apk.gfan.com/games_101_1_1.html","http://apk.gfan.com/games_44_1_1.html","http://apk.gfan.com/games_45_1_1.html","http://apk.gfan.com/games_36_1_1.html","http://apk.gfan.com/games_39_1_1.html","http://apk.gfan.com/games_41_1_1.html","http://apk.gfan.com/games_42_1_1.html","http://apk.gfan.com/games_40_1_1.html","http://apk.gfan.com/games_37_1_1.html","http://apk.gfan.com/games_43_1_1.html"]
    DETAIL_URLS="//div[@class='list-page']/ul[@class='lp-app-list clearfix']/li/p[@class='lp-app-hot']/span[@class='apphot-tit']/a"
    DOWNLOAD_URL="//div[@class='app-descr clearfix']/div[@class='descr-left']/div[@class='app-view-bt']/a[@id='computerLoad']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//h4[@class='curr-tit']"
    CATEGORY="//h3[@class='curr-site']"
    UPLOAD_TIME="//div[@class='app-infoAintro']/div[@class='app-info']/p[3]"
    RATING="//div[@class='descr-left']/span[@class='app-marking png']"

    def get_rating(self,detail_page_driver):
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.text)*10)
        except Exception as e:
            return None
        return rating

    def get_category(self,detail_page_driver):
        try:
            ele = detail_page_driver.find_element_by_xpath(self.CATEGORY)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            category=ele.text.split(">")[2].split("(")[0]
        except Exception as e:
             return None
        return category
