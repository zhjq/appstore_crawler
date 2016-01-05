# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="android.25pp.com"
    START_URLS=["http://android.25pp.com/software/1001_0_0_1.html","http://android.25pp.com/software/1002_0_0_1.html","http://android.25pp.com/software/1003_0_0_1.html","http://android.25pp.com/software/1004_0_0_1.html","http://android.25pp.com/software/1005_0_0_1.html","http://android.25pp.com/software/1006_0_0_1.html","http://android.25pp.com/software/1007_0_0_1.html","http://android.25pp.com/software/1008_0_0_1.html","http://android.25pp.com/game/2001_0_0_1.html","http://android.25pp.com/game/2002_0_0_1.html","http://android.25pp.com/game/2003_0_0_1.html","http://android.25pp.com/game/2004_0_0_1.html","http://android.25pp.com/game/2005_0_0_1.html","http://android.25pp.com/game/2006_0_0_1.html","http://android.25pp.com/game/2007_0_0_1.html","http://android.25pp.com/game/2008_0_0_1.html"]
    DETAIL_URLS="//div[@class='thelist']/dl[@class='setHover apps']/dd[@class='app_title']/h4/a"
    DOWNLOAD_URL="//div[@class='aboutIntr']/div[@class='aoubtL']/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='title-stat']/div[@class='txt']/h1"
    CATEGORY="//div[@class='location']/a[3]"
    DOWNLOAD_COUNT="//div[@class='downMunber']/ul/li[1]/span"
    RATING="//div[@class='downMunber']/ul/li[3]/span"

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
