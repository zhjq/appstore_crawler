# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.shouyouzhijia.net"
    START_URLS=["http://www.shouyouzhijia.net/online_17","http://www.shouyouzhijia.net/online_18","http://www.shouyouzhijia.net/online_19","http://www.shouyouzhijia.net/online_20","http://www.shouyouzhijia.net/online_22","http://www.shouyouzhijia.net/online_21","http://www.shouyouzhijia.net/game_1","http://www.shouyouzhijia.net/game_2","http://www.shouyouzhijia.net/game_14","http://www.shouyouzhijia.net/game_4","http://www.shouyouzhijia.net/game_5","http://www.shouyouzhijia.net/game_6","http://www.shouyouzhijia.net/game_7","http://www.shouyouzhijia.net/game_8","http://www.shouyouzhijia.net/game_9","http://www.shouyouzhijia.net/game_10","http://www.shouyouzhijia.net/game_11","http://www.shouyouzhijia.net/game_12","http://www.shouyouzhijia.net/game_13","http://www.shouyouzhijia.net/game_3","http://www.shouyouzhijia.net/game_15"]
    DETAIL_URLS="//div[@class='category']/dl/dt/a"
    DOWNLOAD_URL="//a[@class='app_freedown ']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//h1[@class='name']"
    CATEGORY="//div[@class=' description_detail']/span[5]/i"
    RATING="//p[@class='star']/img"
    UPLOAD_TIME="//div[@class=' description_detail']/span[4]/i"

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("src").split("star")[1].split(".")[0])*20)
        except Exception as e:
            return None
        return rating
