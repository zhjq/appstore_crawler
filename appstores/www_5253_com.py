# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.5253.com"
    START_URLS=["http://www.5253.com/game/list-1-0-cltf-0-0-0-0-0-1-0-time.html","http://www.5253.com/game/list-1-0-dzyx-0-0-0-0-0-1-0-time.html","http://www.5253.com/game/list-1-0-fxsj-0-0-0-0-0-1-0-time.html","http://www.5253.com/game/list-1-0-jsby-0-0-0-0-0-1-0-time.html","http://www.5253.com/game/list-1-0-mnjy-0-0-0-0-0-1-0-time.html","http://www.5253.com/game/list-1-0-mxjm-0-0-0-0-0-1-0-time.html","http://www.5253.com/game/list-1-0-qpzy-0-0-0-0-0-1-0-time.html","http://www.5253.com/game/list-1-0-scjs-0-0-0-0-0-1-0-time.html","http://www.5253.com/game/list-1-0-tyyd-0-0-0-0-0-1-0-time.html","http://www.5253.com/game/list-1-0-xxyz-0-0-0-0-0-1-0-time.html","http://www.5253.com/game/list-1-0-yyjz-0-0-0-0-0-1-0-time.html"] 
    DETAIL_URLS="//div[@class='result_wrap']/ul/li/div[2]/a"
    DOWNLOAD_URL="//div[@class='dwl-btn']/a[1]"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='game-txtinfo']/h3"
    CATEGORY="//div[@class='game-txtinfo']/div[@class='g-info']/a/span"
    UPLOAD_TIME="//div[@class='dtab-cont dtab-cont-az']/div/div/div[2]/div[1]/p[2]"
    DOWNLOAD_COUNT="//div[@class='dtab-cont dtab-cont-az']/div/div/div[2]/div[1]/p[1]/span"
    RATING="//h5[@id='scoreValue']"

    def get_upload_time(self,detail_page_driver):
        if self.UPLOAD_TIME is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.UPLOAD_TIME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            upload_time = util.unify_data(ele.text.split("更新时间：")[1])
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
            rating = str(float(ele.text)*10)
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
            ele.click()
            download_ele = detail_page_driver.find_element_by_xpath("//div[@class='dtab-cont dtab-cont-az']/div/div/div[2]/div[2]/a[1]")
            download_url = download_ele.get_attribute("data-url")
        except:
            return None
        return download_url
    