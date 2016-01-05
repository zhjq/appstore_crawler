# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.pc6.com"
    START_URLS=["http://www.pc6.com/android/588_1.html","http://www.pc6.com/android/584_1.html","http://www.pc6.com/android/582_1.html","http://www.pc6.com/android/583_1.html","http://www.pc6.com/android/585_1.html","http://www.pc6.com/android/586_1.html","http://www.pc6.com/android/587_1.html","http://www.pc6.com/android/qq_590_1.html","http://www.pc6.com/android/589_1.html","http://www.pc6.com/android/600_1.html","http://www.pc6.com/android/627_1.html","http://www.pc6.com/android/628_1.html","http://www.pc6.com/android/qq_703_1.html","http://www.pc6.com/android/qq_704_1.html","http://www.pc6.com/android/qq_705_1.html","http://www.pc6.com/android/qq_706_1.html","http://www.pc6.com/android/qq_708_1.html","http://www.pc6.com/android/qq_709_1.html","http://www.pc6.com/andyx/594_1.html","http://www.pc6.com/andyx/591_1.html","http://www.pc6.com/andyx/592_1.html","http://www.pc6.com/andyx/593_1.html","http://www.pc6.com/andyx/595_1.html","http://www.pc6.com/andyx/596_1.html","http://www.pc6.com/andyx/598_1.html","http://www.pc6.com/andyx/597_1.html","http://www.pc6.com/andyx/637_1.html","http://www.pc6.com/andyx/638_1.html","http://www.pc6.com/andyx/711_1.html","http://www.pc6.com/andyx/712_1.html","http://www.pc6.com/andyx/713_1.html","http://www.pc6.com/andyx/714_1.html","http://www.pc6.com/andyx/842_1.html","http://www.pc6.com/awangyou/631_1.html","http://www.pc6.com/awangyou/632_1.html","http://www.pc6.com/awangyou/633_1.html","http://www.pc6.com/awangyou/634_1.html","http://www.pc6.com/awangyou/636_1.html","http://www.pc6.com/awangyou/694_1.html","http://www.pc6.com/awangyou/695_1.html","http://www.pc6.com/awangyou/696_1.html","http://www.pc6.com/awangyou/697_1.html","http://www.pc6.com/awangyou/700_1.html"]
    DETAIL_URLS="//dd[@class='rmain']/ul/li/a"
    DOWNLOAD_URL="//ul[@class='ul_Address']/li[last()]/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='fixed']/h1"
    UPLOAD_TIME="//div[@class='fixed']/p[4]/i[3]"
    CATEGORY="//p[@class='seat']/a[3]|div[@class='left3']/div[1]"
    RATING="//div[@class='fixed']/p[4]/i[6]/span"

    def get_upload_time(self,detail_page_driver):
        if self.UPLOAD_TIME is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.UPLOAD_TIME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            upload_time = util.unify_data(ele.text.split("更新：")[1])
        except Exception as e:
            return None
        return upload_time

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            logger.warn("详情页: "+util.get_current_url(detail_page_driver)+" 找不到rating")
            return None
        try:
            rating = str(float(ele.get_attribute("class").split("star")[1])*20)
        except Exception as e:
            return None
        return rating
