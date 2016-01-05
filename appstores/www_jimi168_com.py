# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.jimi168.com"
    START_URLS=["http://www.jimi168.com/SecondHot/1101","http://www.jimi168.com/SecondHot/0601","http://www.jimi168.com/SecondHot/0801","http://www.jimi168.com/SecondHot/0401","http://www.jimi168.com/SecondHot/1301","http://www.jimi168.com/SecondHot/0201","http://www.jimi168.com/SecondHot/0901","http://www.jimi168.com/SecondHot/0501","http://www.jimi168.com/SecondHot/4001","http://www.jimi168.com/SecondHot/3201","http://www.jimi168.com/SecondHot/2601","http://www.jimi168.com/SecondHot/2501","http://www.jimi168.com/SecondHot/3101","http://www.jimi168.com/SecondHot/1901","http://www.jimi168.com/SecondHot/2001","http://www.jimi168.com/SecondHot/2401","http://www.jimi168.com/SecondHot/3401","http://www.jimi168.com/SecondHot/3301","http://www.jimi168.com/SecondHot/3501"]
    DETAIL_URLS="//div[@class='title4']/a"
    DOWNLOAD_URL="//div[@class='jimi_left1']/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='jimi_tit1']/b"
    CATEGORY="//div[@class='posi']/a[3]"
    DOWNLOAD_COUNT="//div[@class='APP_left3_1']"
    UPLOAD_TIME="//div[@class='APP_left3_1']"
    RATING="//div[@class='jimi_tit1']/span"

    def get_download_count(self,detail_page_driver):
        try:
            ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_COUNT)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            download_count = util.unify_download_count(ele.text.split("下载次数：")[1].split('次')[0].strip())
        except Exception as e:
            return None
        return download_count

    def get_upload_time(self,detail_page_driver):
        try:
            ele = detail_page_driver.find_element_by_xpath(self.UPLOAD_TIME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            upload_time = util.unify_data(ele.text.split("更新：")[1].split('版本')[0].strip())
        except Exception as e:
            return None
        return upload_time

    def get_appname(self,detail_page_driver):
        try:
            ele = detail_page_driver.find_element_by_xpath(self.APPNAME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            appName=ele.text.split('--')[0].strip()
        except Exception as e:
            return ele.text.strip()
        return appName

    def get_rating(self,detail_page_driver):
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("title").split("评分：")[1])*20)
        except Exception as e:
            return None
        return rating

