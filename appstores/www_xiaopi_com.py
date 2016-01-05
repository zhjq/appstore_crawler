# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.xiaopi.com"
    START_URLS=["http://www.xiaopi.com/list_0_1_1_0_0_1.html","http://www.xiaopi.com/list_0_1_2_0_0_1.html","http://www.xiaopi.com/list_0_1_3_0_0_1.html","http://www.xiaopi.com/list_0_1_4_0_0_1.html","http://www.xiaopi.com/list_0_1_5_0_0_1.html","http://www.xiaopi.com/list_0_1_6_0_0_1.html","http://www.xiaopi.com/list_0_1_7_0_0_1.html","http://www.xiaopi.com/list_0_1_8_0_0_1.html","http://www.xiaopi.com/list_0_1_9_0_0_1.html","http://www.xiaopi.com/list_0_1_10_0_0_1.html","http://www.xiaopi.com/list_0_1_11_0_0_1.html","http://www.xiaopi.com/list_0_1_12_0_0_1.html"]
    DETAIL_URLS="//div[@class='yx_list clearfix']/div/div[@class='info']/h5/a"
    DOWNLOAD_URL="//ul[@class='clearfix']/li[@class='az tiaz']/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='tit']"
    CATEGORY="//div[@id='zcgs']/div[@class='show_l3']/p[2]/span[1]"
    RATING="//div[@id='zcgs']/div[@class='show_l1']/i[@class='fenshu']/em"

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.text)*10)
        except Exception as e:
            return None
        return rating