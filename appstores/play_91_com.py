# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="play.91.com"
    START_URLS=["http://play.91.com/android/Soft/index-18.html","http://play.91.com/android/Soft/index-20.html","http://play.91.com/android/Soft/index-17.html","http://play.91.com/android/Soft/index-19.html","http://play.91.com/android/Soft/index-25.html","http://play.91.com/android/Soft/index-23.html","http://play.91.com/android/Soft/index-32.html","http://play.91.com/android/Soft/index-37.html","http://play.91.com/android/Soft/index-30.html","http://play.91.com/android/Soft/index-31.html","http://play.91.com/android/Soft/index-28.html","http://play.91.com/android/Soft/index-36.html","http://play.91.com/android/Soft/index-27.html","http://play.91.com/android/Soft/index-39.html","http://play.91.com/android/Soft/index-29.html","http://play.91.com/android/Soft/index-26.html","http://play.91.com/android/Soft/index-21.html","http://play.91.com/android/Soft/index-35.html","http://play.91.com/android/Soft/index-24.html","http://play.91.com/android/Soft/index-44.html","http://play.91.com/android/Soft/index-42.html","http://play.91.com/android/Soft/index-33.html","http://play.91.com/android/Soft/index-22.html","http://play.91.com/android/Soft/index-40.html","http://play.91.com/android/Game/index-3.html","http://play.91.com/android/Game/index-10.html","http://play.91.com/android/Game/index-4.html","http://play.91.com/android/Game/index-2.html","http://play.91.com/android/Game/index-12.html","http://play.91.com/android/Game/index-11.html","http://play.91.com/android/Game/index-8.html","http://play.91.com/android/Game/index-5.html","http://play.91.com/android/Game/index-14.html","http://play.91.com/android/Game/index-13.html","http://play.91.com/android/Game/index-7.html","http://play.91.com/android/Game/index-9.html","http://play.91.com/android/Game/index-6.html","http://play.91.com/android/Game/index-15.html"]
    DETAIL_URLS="//div[@class='w-870 mt-15 fl']/ul[@class='ss-list mt-10 clearfix']/li/div/div/h4/a"
    DOWNLOAD_URL="//span[@class='ssoft-btns']/a[@class='s-down-btn-1']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//h1[@class='ssoft-name']"
    UPLOAD_TIME="//div[@class='ssoft-intro-box mt-40 clearfix']/span[4]"
    RATING="//em[@class='ssoft-score']"
    CATEGORY="//div[@class='ssoft-intro-box mt-40 clearfix']/span[5]"
    UPLOAD_TIME="//div[@class='ssoft-intro-box mt-40 clearfix']/span[4]"

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
