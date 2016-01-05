# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.doyo.cn"
    START_URLS=["http://www.doyo.cn/shouji/list/101/1/1/1/1","http://www.doyo.cn/shouji/list/102/1/1/1/1","http://www.doyo.cn/shouji/list/103/1/1/1/1","http://www.doyo.cn/shouji/list/104/1/1/1/1","http://www.doyo.cn/shouji/list/105/1/1/1/1","http://www.doyo.cn/shouji/list/106/1/1/1/1","http://www.doyo.cn/shouji/list/107/1/1/1/1","http://www.doyo.cn/shouji/list/108/1/1/1/1","http://www.doyo.cn/shouji/list/109/1/1/1/1","http://www.doyo.cn/shouji/list/110/1/1/1/1","http://www.doyo.cn/shouji/list/111/1/1/1/1","http://www.doyo.cn/shouji/list/112/1/1/1/1","http://www.doyo.cn/shouji/list/113/1/1/1/1","http://www.doyo.cn/shouji/list/114/1/1/1/1"]
    DETAIL_URLS="//div[@class='game_list']/div/a[@class='name']"
    DOWNLOAD_URL="//head/script[7]"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='gameName']/h1"
    CATEGORY="//div[@class='xx']/a"
    UPLOAD_TIME="//div[@class='xx']"
    DOWNLOAD_COUNT="//div[@class='xx']"
    RATING="//div[@class='score']/strong"

    def get_upload_time(self,detail_page_driver):
        if self.UPLOAD_TIME is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.UPLOAD_TIME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            upload_time = util.unify_data(ele.text.split("更新：")[1])
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
            download_count = util.unify_download_count(ele.text.split("\n")[0].split(" ")[4].split("次")[0])
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
            rating = str(float(ele.text.split("分")[0])*10)
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
            download_url = ele.get_attribute("textContent").split("\"")[5].split("\"")[0]
        except:
            pass
        return download_url
