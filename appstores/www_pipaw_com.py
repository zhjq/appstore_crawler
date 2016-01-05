# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.pipaw.com"
    START_URLS=["http://www.pipaw.com/apps/android-ltsj/","http://www.pipaw.com/apps/android-spyy/","http://www.pipaw.com/apps/android-gwsc/","http://www.pipaw.com/apps/android-bgrj/","http://www.pipaw.com/apps/android-sjmh/","http://www.pipaw.com/apps/android-dhtx/","http://www.pipaw.com/apps/android-jrlc/","http://www.pipaw.com/apps/android-shfw/","http://www.pipaw.com/apps/android-xwyd/","http://www.pipaw.com/apps/android-jtdh/","http://www.pipaw.com/apps/android-lycx/","http://www.pipaw.com/apps/android-xtgj/"] 
    DETAIL_URLS="//div[@class='lib_left_list']/dl/dd/p[1]/span[1]/a"
    DOWNLOAD_URL="//div[@class='download_left']/dl/dd/p[1]/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='download_left']/dl/dt/p[1]/a/span"
    CATEGORY="//div[@class='dload_mes']/table/tbody/tr[1]/td[1]/a"
    UPLOAD_TIME="//div[@class='dload_mes']/table/tbody/tr[2]/td[4]/span"
    DOWNLOAD_COUNT="//div[@class='dload_mes']/table/tbody/tr[2]/td[3]/span"
    RATING="//div[@class='download_left']/dl/dt/p[2]/span"

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.text)*20)
        except Exception as e:
            return None
        return rating
    
