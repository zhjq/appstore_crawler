# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.duote.com"
    START_URLS=["http://www.duote.com/android/game_220.html","http://www.duote.com/android/game_233.html","http://www.duote.com/android/game_224.html","http://www.duote.com/android/game_229.html","http://www.duote.com/android/game_223.html","http://www.duote.com/android/game_225.html","http://www.duote.com/android/game_222.html","http://www.duote.com/android/game_230.html","http://www.duote.com/android/game_226.html","http://www.duote.com/android/game_231.html","http://www.duote.com/android/soft_201.html","http://www.duote.com/android/soft_202.html","http://www.duote.com/android/soft_210.html","http://www.duote.com/android/soft_211.html","http://www.duote.com/android/soft_212.html","http://www.duote.com/android/soft_213.html","http://www.duote.com/android/soft_219.html","http://www.duote.com/android/soft_214.html","http://www.duote.com/android/soft_217.html","http://www.duote.com/android/soft_215.html","http://www.duote.com/android/soft_209.html","http://www.duote.com/android/soft_216.html","http://www.duote.com/android/soft_218.html","http://www.duote.com/android/soft_206.html"]
    DETAIL_URLS="//div[@class='Mlist']/div[@class='list_item']/div[@class='tit_area']/span[@class='name']/a"
    DOWNLOAD_URL="//div[@class='dl_area']/div[@class='btn_trig']/a[@id='quickDown']"
    NEXTPAGE="//a[text()='下一页']"
    CATEGORY="//div[@class='crumb']/a[3]"
    APPNAME="//div[@class='tit_area clearfix']/h1"
    UPLOAD_TIME="//ul[@class='prop_area']/li[3]"
    DOWNLOAD_COUNT="//ul[@class='prop_area']/li[2]"
    RATING="//span[@class='level_big']/i"

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("style").split(" ")[1].split("%")[0]))
        except Exception as e:
            return None
        return rating