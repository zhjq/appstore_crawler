# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="appstore.huawei.com"
    START_URLS=["http://appstore.huawei.com/soft/list_23_2","http://appstore.huawei.com/soft/list_27_2","http://appstore.huawei.com/soft/list_28_2","http://appstore.huawei.com/soft/list_26_2","http://appstore.huawei.com/soft/list_24_2","http://appstore.huawei.com/soft/list_33_2","http://appstore.huawei.com/soft/list_29_2","http://appstore.huawei.com/soft/list_35_2","http://appstore.huawei.com/soft/list_345_2","http://appstore.huawei.com/soft/list_30_2","http://appstore.huawei.com/soft/list_25_2","http://appstore.huawei.com/soft/list_31_2","http://appstore.huawei.com/soft/list_34_2","http://appstore.huawei.com/game/list_17_2","http://appstore.huawei.com/game/list_15_2","http://appstore.huawei.com/game/list_22_2","http://appstore.huawei.com/game/list_21_2","http://appstore.huawei.com/game/list_19_2","http://appstore.huawei.com/game/list_18_2","http://appstore.huawei.com/game/list_16_2","http://appstore.huawei.com/game/list_20_2"]
    DETAIL_URLS="//div[@class='game-info  whole']/h4/a"
    DOWNLOAD_URL="//a[@class='mkapp-btn mab-download']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='app-info flt']/ul[1]/li[2]/p[1]/span[1]"
    UPLOAD_TIME="//ul[@class='app-info-ul nofloat'][2]/li[2]/span"
    DOWNLOAD_COUNT="//span[@class='grey sub']"
    RATING="//ul[@class='app-info-ul nofloat'][1]/li[2]/p[2]/span"

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("class").split('score_')[1])*10)
        except Exception as e:
            return None
        return rating

    def get_download_url(self,detail_page_driver):
        download_url = None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_URL)
        except selenium_exception.NoSuchElementException as e:
            detail_page_driver.refresh()
            try:
                ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_URL)
            except selenium_exception.NoSuchElementException as e:
                return download_url
        try:
            download_url = ele.get_attribute("onclick").split(",")[5].split("'")[1]
        except Exception as e:
            pass
        return download_url
