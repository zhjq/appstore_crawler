# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.fpwap.com"
    START_URLS=["http://www.fpwap.com/gamelist/2-1-0-0-0-0-1.html","http://www.fpwap.com/gamelist/2-2-0-0-0-0-1.html","http://www.fpwap.com/gamelist/2-3-0-0-0-0-1.html","http://www.fpwap.com/gamelist/2-4-0-0-0-0-1.html","http://www.fpwap.com/gamelist/2-5-0-0-0-0-1.html","http://www.fpwap.com/gamelist/2-6-0-0-0-0-1.html","http://www.fpwap.com/gamelist/2-7-0-0-0-0-1.html","http://www.fpwap.com/gamelist/2-8-0-0-0-0-1.html"]
    DETAIL_URLS="//div[@class='game-poker-con']/ul/li/a[@class='info']"
    DOWNLOAD_URL="//a[@id='m_down_and']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//dl[@class='game-title']/dd/h1"
    CATEGORY="//p[@class='dn-game-type mtb10']/a[1]"
    RATING="//div[@class='fr fp-number']"

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
