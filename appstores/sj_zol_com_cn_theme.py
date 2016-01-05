# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="sj.zol.com.cn"
    START_URLS=["http://sj.zol.com.cn/sys_sub/sub84_3_1_1.html"]
    DETAIL_URLS="//ul[@class='soft-list clearfix']/li/h4/a"
    DOWNLOAD_URL="//div[@class='down-button-box h-down-box']/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//h1[@class='soft-title']"
    CATEGORY="//div[@class='nav-path']/a[4]"
    RATING="//ul[@class='soft-infor']/li[4]/em"
    DOWNLOAD_COUNT="//ul[@class='soft-infor']/li[5]"

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
