# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="android.d.cn"
    START_URLS=["http://android.d.cn/game/list_1_0_6_0_0_0_0_0_0_0_0_1_0.html","http://android.d.cn/software/list_1_19_0.html","http://android.d.cn/software/list_1_24_0.html","http://android.d.cn/game/list_1_0_8_0_0_0_0_0_0_0_0_1_0.html","http://android.d.cn/software/list_1_29_0.html","http://android.d.cn/game/list_1_0_4_0_0_0_0_0_0_0_0_1_0.html","http://android.d.cn/software/list_1_22_0.html","http://android.d.cn/game/list_1_0_5_0_0_0_0_0_0_0_0_1_0.html","http://android.d.cn/software/list_1_27_0.html","http://android.d.cn/game/list_1_0_14_0_0_0_0_0_0_0_0_1_0.html","http://android.d.cn/software/list_1_33_0.html","http://android.d.cn/game/list_1_0_9_0_0_0_0_0_0_0_0_1_0.html","http://android.d.cn/software/list_1_49_0.html","http://android.d.cn/game/list_1_0_10_0_0_0_0_0_0_0_0_1_0.html","http://android.d.cn/software/list_1_20_0.html","http://android.d.cn/game/list_1_0_11_0_0_0_0_0_0_0_0_1_0.html","http://android.d.cn/software/list_1_25_0.html","http://android.d.cn/game/list_1_0_12_0_0_0_0_0_0_0_0_1_0.html","http://android.d.cn/software/list_1_30_0.html","http://android.d.cn/game/list_1_0_13_0_0_0_0_0_0_0_0_1_0.html","http://android.d.cn/software/list_1_18_0.html","http://android.d.cn/game/list_1_0_15_0_0_0_0_0_0_0_0_1_0.html","http://android.d.cn/software/list_1_23_0.html","http://android.d.cn/game/list_1_0_16_0_0_0_0_0_0_0_0_1_0.html","http://android.d.cn/software/list_1_28_0.html","http://android.d.cn/game/list_1_0_48_0_0_0_0_0_0_0_0_1_0.html","http://android.d.cn/software/list_1_34_0.html","http://android.d.cn/software/list_1_50_0.html","http://android.d.cn/software/list_1_21_0.html","http://android.d.cn/software/list_1_26_0.html","http://android.d.cn/software/list_1_31_0.html","http://android.d.cn/game/list_1_0_7_0_0_0_0_0_0_0_0_1_0.html"]
    DETAIL_URLS="//div[@class='left']/ul/li/div[@class='list-in']/div[@class='list-right']/p[@class='g-name']/a"
    DOWNLOAD_URL="//ul[@class='de-down']/li[1]/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='de-head-l']/h1|//h1[@class='notag']"
    CATEGORY="//ul[@class='de-game-info clearfix']/li[1]/a"
    RATING="//ul[@class='de-game-info clearfix']/li[5]/span[2]/span"
    UPLOAD_TIME="//ul[@class='de-game-info clearfix']/li[3]"
    def get_download_url(self,detail_page_driver):
        try:
            ele = detail_page_driver.find_element_by_xpath("//ul[@class='de-app-tip clearfix']/li[4]")
        except selenium_exception.NoSuchElementException as e:
            pass
        else:
            apk_or_dpk=ele.text.strip()
            if not apk_or_dpk=="APK":
                return None
        download_url = None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_URL)
        except selenium_exception.NoSuchElementException as e:
            try:
                detail_page_driver.refresh()
            except selenium_exception.TimeoutException as e:
                pass
            try:
                ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_URL)
            except selenium_exception.NoSuchElementException as e:
                return download_url
        try:
            download_url = ele.get_attribute('onclick').split("'")[1]
        except Exception as e:
            return download_url
        return download_url

    def get_rating(self,detail_page_driver):
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("class").split("stars-")[1])*20)
        except Exception as e:
            return None
        return rating
