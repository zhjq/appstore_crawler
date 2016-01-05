# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.289.com"
    START_URLS=["http://www.289.com/ku/1_2-2_0-3_8-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_7-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_6-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_24-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_20-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_11-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_10-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_9-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_23-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_79-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_25-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_77-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_22-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_21-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_12-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_13-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_14-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_15-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_16-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_17-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_18-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_19-13_0_sd/","http://www.289.com/ku/1_2-2_0-3_81-13_0_sd/"] 
    DETAIL_URLS="//ul[@class='gm-list clearfix']/li/dl/dt/h3/a"
    DOWNLOAD_URL="//div[@class='ku_xiazai2']/a[last()]"
    NEXTPAGE="//a[@class='next']"
    APPNAME="//h1[@class='m_tit f-fl']/a"
    CATEGORY="//ul[@class='f-cle f-lifl']/li[6]/a[1]"
    UPLOAD_TIME="//ul[@class='m-listnew f-cle']/li/p[1]"

    def get_upload_time(self,detail_page_driver):
        if self.UPLOAD_TIME is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.UPLOAD_TIME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            upload_time = util.unify_data(ele.text.split("更新时间：")[1])
        except Exception as e:
            return None
        return upload_time
