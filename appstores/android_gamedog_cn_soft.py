# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="android.gamedog.cn"
    START_URLS=["http://android.gamedog.cn/list_soft_0_170_0_0_0_0.html","http://android.gamedog.cn/list_soft_0_177_0_0_0_0.html","http://android.gamedog.cn/list_soft_0_529_0_0_0_0.html","http://android.gamedog.cn/list_soft_0_178_0_0_0_0.html","http://android.gamedog.cn/list_soft_0_174_0_0_0_0.html","http://android.gamedog.cn/list_soft_0_179_0_0_0_0.html","http://android.gamedog.cn/list_soft_0_173_0_0_0_0.html","http://android.gamedog.cn/list_soft_0_172_0_0_0_0.html","http://android.gamedog.cn/list_soft_0_528_0_0_0_0.html","http://android.gamedog.cn/list_soft_0_530_0_0_0_0.html","http://android.gamedog.cn/list_soft_0_175_0_0_0_0.html","http://android.gamedog.cn/list_soft_0_531_0_0_0_0.html","http://android.gamedog.cn/list_soft_0_526_0_0_0_0.html","http://android.gamedog.cn/list_soft_0_527_0_0_0_0.html","http://android.gamedog.cn/list_soft_0_1093_0_0_0_0.html","http://android.gamedog.cn/list_soft_0_582_0_0_0_0.html"]
    DETAIL_URLS="//ul[@class='list_yc_big']/li/a"
    DOWNLOAD_URL="//dd[@class='xiazai']/span[1]/a"
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