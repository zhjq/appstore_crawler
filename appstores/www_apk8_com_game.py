# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.apk8.com"
    START_URLS=["http://www.apk8.com/wy/list_17_1.html","http://www.apk8.com/list/list_2_1.html","http://www.apk8.com/list/list_3_1.html","http://www.apk8.com/list/list_5_1.html","http://www.apk8.com/list/list_6_1.html","http://www.apk8.com/list/list_7_1.html","http://www.apk8.com/list/list_8_1.html","http://www.apk8.com/list/list_9_1.html","http://www.apk8.com/list/list_10_1.html","http://www.apk8.com/list/list_11_1.html","http://www.apk8.com/list/list_14_1.html","http://www.apk8.com/list/list_1_1.html","http://www.apk8.com/list/list_15_1.html","http://www.apk8.com/list/list_86_1.html","http://www.apk8.com/list/list_62_1.html","http://www.apk8.com/list/list_38_1.html","http://www.apk8.com/list/list_76_1.html","http://www.apk8.com/wy/list_18_1.html","http://www.apk8.com/wy/list_88_1.html","http://www.apk8.com/wy/list_89_1.html"]
    DETAIL_URLS="//div[@class='main_list_list']/div[@class='main_list_pic']/ul/li/strong/a"
    DOWNLOAD_URL="//div[@class='downnew1']/div[@class='downnew']/a[@class='bt_tx2']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='tit_b']"
    CATEGORY="//div[@class='game_info_main']/div[@class='game_info_location']/a[3]"
    UPLOAD_TIME="//div[@class='detailsleft']/ol[4]/li"
    DOWNLOAD_COUNT="//div[@class='game_info_left_n_1']/span[@id='downNum']"
    RATING="//div[@class='game_info_left_n_1']/img"

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
            rating = str(float(ele.get_attribute("src").split("_")[2].split(".")[0])*20)
        except Exception as e:
            return None
        return rating
    
    def get_download_url(self,detail_page_driver):
        download_url = None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_URL)
        except selenium_exception.NoSuchElementException as e:
            detail_page_driver.refresh()
            try:
                ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_URL)
            except selenium_exception.NoSuchElementException as e:
                return download_url
        try:
            download_url = ele.get_attribute("href")
            if download_url == "http://www.baidu.com/" :
                return None
        except:
            return None
        return download_url
