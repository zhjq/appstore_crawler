# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="sj.skycn.com"
    START_URLS=["http://sj.skycn.com/soft/android/1_1_77_1.html","http://sj.skycn.com/soft/android/1_1_72_1.html","http://sj.skycn.com/soft/android/1_1_75_1.html","http://sj.skycn.com/soft/android/1_1_76_1.html","http://sj.skycn.com/soft/android/1_1_73_1.html","http://sj.skycn.com/soft/android/1_1_79_1.html","http://sj.skycn.com/soft/android/1_1_80_1.html","http://sj.skycn.com/soft/android/1_1_84_1.html","http://sj.skycn.com/soft/android/1_1_88_1.html","http://sj.skycn.com/soft/android/1_1_74_1.html","http://sj.skycn.com/soft/android/1_1_108_1.html","http://sj.skycn.com/soft/android/1_1_103_1.html","http://sj.skycn.com/soft/android/1_1_107_1.html","http://sj.skycn.com/soft/android/1_1_65_1.html","http://sj.skycn.com/soft/android/1_1_110_1.html","http://sj.skycn.com/soft/android/1_1_109_1.html","http://sj.skycn.com/soft/android/1_1_78_1.html","http://sj.skycn.com/soft/android/1_1_64_1.html","http://sj.skycn.com/soft/android/1_1_66_1.html","http://sj.skycn.com/soft/android/1_1_81_1.html","http://sj.skycn.com/soft/android/1_1_70_1.html","http://sj.skycn.com/soft/android/1_1_69_1.html","http://sj.skycn.com/soft/android/1_1_62_1.html","http://sj.skycn.com/soft/android/1_1_87_1.html","http://sj.skycn.com/soft/android/1_1_106_1.html","http://sj.skycn.com/soft/android/1_1_85_1.html","http://sj.skycn.com/soft/android/1_1_68_1.html","http://sj.skycn.com/soft/android/1_1_83_1.html"]
    DETAIL_URLS="//ul[@class='list-content-box clearfix']/li/a"
    DOWNLOAD_URL="//a[@class='download-pc download-dlcount']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='info']/h2"
    CATEGORY="//div[@class='breadcrumb']/a[4]"
    RATING="//span[@class='score']"
    UPLOAD_TIME="//div[@class='info']/ul[1]/li[3]"
    DOWNLOAD_COUNT="//div[@class='info']/ul[2]/li[1]"

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