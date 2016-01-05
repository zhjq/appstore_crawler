# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="game.11773.com"
    START_URLS=["http://game.11773.com/android_dongzuo/","http://game.11773.com/android_zhuomian/","http://game.11773.com/android_yinyue/","http://game.11773.com/android_zhili/","http://game.11773.com/android_saiche/","http://game.11773.com/android_rpg/","http://game.11773.com/android_moni/","http://game.11773.com/android_tiyu/","http://game.11773.com/android_celue/","http://game.11773.com/android_xiaoyx/"] 
    DETAIL_URLS="//div[@class='clearfix gamelist']/dl/a"
    DOWNLOAD_URL="//div[@class='c-right']/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='game_detail_title clearfix']/h2/a"
    CATEGORY="//ul[@class='game_aside_intro']/li[5]/span/a"
    UPLOAD_TIME="//div[@class='game_download_list android_bg']/dl/dd[1]/p/em[2]/span"
    RATING="//span[@class='game_good f14']/b"

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.text.split("%")[0]))
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
            download_url = ele.get_attribute("onclick").split("\'")[1].split("\'")[0]
        except:
            return None
        return download_url
