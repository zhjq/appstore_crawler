# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.25az.com"
    START_URLS=["http://www.25az.com/android/Sort/PVP/","http://www.25az.com/android/Sort/RPG/","http://www.25az.com/android/Sort/PUZ/","http://www.25az.com/android/Sort/ARPG/","http://www.25az.com/android/Sort/ACT/","http://www.25az.com/android/Sort/SLG/","http://www.25az.com/android/Sort/RAC/","http://www.25az.com/android/Sort/FLY/","http://www.25az.com/android/Sort/DEV/","http://www.25az.com/android/Sort/SPG/","http://www.25az.com/android/Sort/AVG/","http://www.25az.com/android/Sort/STG/","http://www.25az.com/android/Sort/CHG/","http://www.25az.com/android/Sort/SIM/","http://www.25az.com/android/Sort/FTG/","http://www.25az.com/android/Sort/TCG/","http://www.25az.com/android/Sort/MUG/","http://www.25az.com/android/Sort/FPS/","http://www.25az.com/android/Sort/RTS/","http://www.25az.com/android/Sort/EDU/","http://www.25az.com/android/Sort/DEC/","http://www.25az.com/android/Sort/GS/","http://www.25az.com/ol/"]
    DETAIL_URLS="//ul[@class='app_list']/li/p[1]/a"
    DOWNLOAD_URL="//a[text()='本地下载']"
    NEXTPAGE="//div[@class='pagenav clearfix']/a[last()-1]"
    APPNAME="//div[@class='app-msg']/h1"
    CATEGORY="//li[@class='bread-now']/a"
    UPLOAD_TIME="//div[@style='margin-left: 82px']/div[last()]"

    def get_upload_time(self,detail_page_driver):
        if self.UPLOAD_TIME is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.UPLOAD_TIME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            upload_time = util.unify_data(ele.text.split("：")[1].split(" ")[0])
        except Exception as e:
            return None
        return upload_time
