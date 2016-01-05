# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.apk8.com"
    START_URLS=["http://www.apk8.com/soft/list_63_1.html","http://www.apk8.com/soft/list_64_1.html","http://www.apk8.com/soft/list_65_1.html","http://www.apk8.com/soft/list_66_1.html","http://www.apk8.com/soft/list_67_1.html","http://www.apk8.com/soft/list_68_1.html","http://www.apk8.com/soft/list_71_1.html","http://www.apk8.com/soft/list_72_1.html","http://www.apk8.com/soft/list_73_1.html","http://www.apk8.com/soft/list_74_1.html"]
    DETAIL_URLS="//div[@class='main_list_list']/div/ul/li/div[@class='list_right']/div[@class='list_title']/a"
    DOWNLOAD_URL="//div[@class='downnew1']/div[@class='downnew']/a[@class='bt_bd']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='tit_b']"
    CATEGORY="//div[@class='game_info_main']/div[@class='game_info_location']/a[3]"
    UPLOAD_TIME="//div[@class='detailsleft']/ol[4]/li"
    DOWNLOAD_COUNT="//div[@class='game_info_left_n_1']/span[@id='downNum']"
    RATING="//div[@class='game_info_left_n_1']/img"

    def get_upload_time(self,detail_page_driver):
        if self.UPLOAD_TIME is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.UPLOAD_TIME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            upload_time = util.unify_data(ele.text.split(" ")[0])
        except Exception as e:
            return None
        return upload_time

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("src").split("_")[2].split(".")[0])*20)
        except Exception as e:
            return None
        return rating
