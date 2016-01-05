# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    REQ_HEADER={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0'}
    SOURCE="apk.91.com"
    START_URLS=["http://apk.91.com/soft/7_1_5","http://apk.91.com/soft/18_1_5","http://apk.91.com/soft/27_1_5","http://apk.91.com/soft/29_1_5","http://apk.91.com/soft/51_1_5","http://apk.91.com/soft/6_1_5","http://apk.91.com/soft/2_1_5","http://apk.91.com/soft/28_1_5","http://apk.91.com/soft/26_1_5","http://apk.91.com/soft/48_1_5","http://apk.91.com/soft/49_1_5","http://apk.91.com/soft/47_1_5","http://apk.91.com/soft/30_1_5","http://apk.91.com/soft/17_1_5","http://apk.91.com/soft/8_1_5","http://apk.91.com/soft/5_1_5","http://apk.91.com/soft/12_1_5","http://apk.91.com/soft/16_1_5","http://apk.91.com/soft/10_1_5","http://apk.91.com/soft/19_1_5","http://apk.91.com/soft/31_1_5","http://apk.91.com/soft/52_1_5","http://apk.91.com/soft/15_1_5","http://apk.91.com/soft/23_1_5","http://apk.91.com/soft/20_1_5","http://apk.91.com/soft/11_1_5","http://apk.91.com/soft/3_1_5","http://apk.91.com/soft/25_1_5","http://apk.91.com/soft/22_1_5","http://apk.91.com/soft/9_1_5","http://apk.91.com/soft/24_1_5","http://apk.91.com/soft/4_1_5","http://apk.91.com/soft/14_1_5","http://apk.91.com/soft/21_1_5","http://apk.91.com/soft/13_1_5","http://apk.91.com/soft/1_1_5","http://apk.91.com/game/34_1_5","http://apk.91.com/game/44_1_5","http://apk.91.com/game/36_1_5","http://apk.91.com/game/35_1_5","http://apk.91.com/game/40_1_5","http://apk.91.com/game/42_1_5","http://apk.91.com/game/33_1_5","http://apk.91.com/game/41_1_5","http://apk.91.com/game/43_1_5","http://apk.91.com/game/39_1_5","http://apk.91.com/game/37_1_5","http://apk.91.com/game/53_1_5","http://apk.91.com/game/45_1_5","http://apk.91.com/game/38_1_5"]
    DETAIL_URLS="//ul[@class='topic_soft_list game_list clearfix']/li/div[1]/div/h4/a"
    DOWNLOAD_URL="//div[@class='fr s_btn_box clearfix']/a[@class='s_btn s_btn4']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='s_title clearfix']/h1"
    CATEGORY="//ul[@class='s_info']/li[last()]/a[1]"
    UPLOAD_TIME="//ul[@class='s_info']/li[5]"
    DOWNLOAD_COUNT="//ul[@class='s_info']/li[2]"
    RATING="//div[@class='s_intro_pic fl']/span[@class='spr star']/a"

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
            rating = str(float(ele.get_attribute("class").split('w')[1].split(' ')[0])*20)
        except Exception as e:
            return None
        return rating
