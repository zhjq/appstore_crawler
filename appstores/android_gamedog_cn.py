# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="android.gamedog.cn"
    START_URLS=["http://android.gamedog.cn/list_online_0_521_0_0_0_0.html","http://android.gamedog.cn/list_online_0_522_0_0_0_0.html","http://android.gamedog.cn/list_online_0_523_0_0_0_0.html","http://android.gamedog.cn/list_online_0_571_0_0_0_0.html","http://android.gamedog.cn/list_online_0_576_0_0_0_0.html","http://android.gamedog.cn/list_online_0_525_0_0_0_0.html","http://android.gamedog.cn/list_online_0_520_0_0_0_0.html","http://android.gamedog.cn/list_game_0_165_0_0_0_0.html","http://android.gamedog.cn/list_game_0_161_0_0_0_0.html","http://android.gamedog.cn/list_game_0_162_0_0_0_0.html","http://android.gamedog.cn/list_game_0_163_0_0_0_0.html","http://android.gamedog.cn/list_game_0_168_0_0_0_0.html","http://android.gamedog.cn/list_game_0_269_0_0_0_0.html","http://android.gamedog.cn/list_game_0_167_0_0_0_0.html","http://android.gamedog.cn/list_game_0_169_0_0_0_0.html","http://android.gamedog.cn/list_game_0_266_0_0_0_0.html","http://android.gamedog.cn/list_game_0_268_0_0_0_0.html","http://android.gamedog.cn/list_game_0_164_0_0_0_0.html","http://android.gamedog.cn/list_game_0_166_0_0_0_0.html","http://android.gamedog.cn/list_game_0_270_0_0_0_0.html","http://android.gamedog.cn/list_game_0_267_0_0_0_0.html","http://android.gamedog.cn/list_game_0_271_0_0_0_0.html"]
    DETAIL_URLS="//ul[@class='list_yc_big']/li/a"
    DOWNLOAD_URL="//dd[@id='downs_box']/span[1]/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//h1[@class='s_title']/span"
    UPLOAD_TIME="//div[@class='info_m']/ul/li[1]/span[1]"
    CATEGORY="//div[@class='info_m']/ul/li[2]/span"
    RATING="//div[@class='info_l']/span[2]/img"

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("alt").split("星")[0])*20)
        except Exception as e:
            return None
        return rating
