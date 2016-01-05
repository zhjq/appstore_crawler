# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.anzhi.com"
    START_URLS=["http://www.anzhi.com/sort_67_1_hot.html","http://www.anzhi.com/sort_69_1_hot.html","http://www.anzhi.com/sort_82_1_hot.html","http://www.anzhi.com/sort_21_1_hot.html","http://www.anzhi.com/sort_84_1_hot.html","http://www.anzhi.com/sort_14_1_hot.html","http://www.anzhi.com/sort_39_1_hot.html","http://www.anzhi.com/sort_15_1_hot.html","http://www.anzhi.com/sort_40_1_hot.html","http://www.anzhi.com/sort_16_1_hot.html","http://www.anzhi.com/sort_41_1_hot.html","http://www.anzhi.com/sort_19_1_hot.html","http://www.anzhi.com/sort_42_1_hot.html","http://www.anzhi.com/sort_20_1_hot.html","http://www.anzhi.com/sort_43_1_hot.html","http://www.anzhi.com/sort_24_1_hot.html","http://www.anzhi.com/sort_44_1_hot.html","http://www.anzhi.com/sort_56_1_hot.html","http://www.anzhi.com/sort_45_1_hot.html","http://www.anzhi.com/sort_57_1_hot.html","http://www.anzhi.com/sort_46_1_hot.html","http://www.anzhi.com/sort_47_1_hot.html","http://www.anzhi.com/sort_48_1_hot.html","http://www.anzhi.com/sort_49_1_hot.html","http://www.anzhi.com/sort_50_1_hot.html","http://www.anzhi.com/sort_51_1_hot.html","http://www.anzhi.com/sort_52_1_hot.html","http://www.anzhi.com/sort_53_1_hot.html","http://www.anzhi.com/sort_54_1_hot.html","http://www.anzhi.com/sort_55_1_hot.html"]
    DETAIL_URLS="//span[@class='app_name']/a"
    DOWNLOAD_URL="//a[text()='下载到电脑']"
    NEXTPAGE="//a[@class='next']"
    APPNAME="//div[@class='detail_description']/div[1]/h3"
    CATEGORY="//div[@class='title']/h2/a"
    RATING="//div[@id='stars_detail']"
    DOWNLOAD_COUNT="//ul[@id='detail_line_ul']/li[2]/span"
    UPLOAD_TIME="//ul[@id='detail_line_ul']/li[3]"

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
            downLoadURLID = ele.get_attribute("onclick").split("(")[1].split(")")[0]
            download_url = "http://" + self.SOURCE + "/dl_app.php?s=" + downLoadURLID
        except Exception as e:
            pass
        return download_url

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        if ele.get_attribute("style") == 'background-position:0 0px;':
            return '0.0'
        if ele.get_attribute("style") == 'background-position:0 -15px;':
            return '15.0'
        if ele.get_attribute("style") == 'background-position:0 -30px;':
            return '20.0'
        if ele.get_attribute("style") == 'background-position:0 -45px;':
            return '30.0'
        if ele.get_attribute("style") == 'background-position:0 -60px;':
            return '40.0'
        if ele.get_attribute("style") == 'background-position:0 -75px;':
            return '50.0'
        if ele.get_attribute("style") == 'background-position:0 -90px;':
            return '60.0'
        if ele.get_attribute("style") == 'background-position:0 -105px;':
            return '70.0'
        if ele.get_attribute("style") == 'background-position:0 -120px;':
            return '80.0'
        if ele.get_attribute("style") == 'background-position:0 -135px;':
            return '90.0'
        if ele.get_attribute("style") == 'background-position:0 -150px;':
            return '100.0'
        return None
