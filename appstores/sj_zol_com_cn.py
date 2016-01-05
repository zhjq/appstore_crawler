# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="sj.zol.com.cn"
    START_URLS=["http://sj.zol.com.cn/sys_sub/sub115_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub72_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub80_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub76_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub79_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub84_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub75_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub73_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub88_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub77_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub74_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub108_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub103_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub107_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub65_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub110_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub109_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub78_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub64_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub66_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub81_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub70_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub69_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub62_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub87_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub106_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub85_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub112_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub68_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub113_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub111_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub83_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub93_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub94_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub89_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub92_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub98_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub97_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub104_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub102_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub90_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub96_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub91_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub95_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub99_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub101_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub105_3_1_1.html","http://sj.zol.com.cn/sys_sub/sub100_3_1_1.html"]
    DETAIL_URLS="//ul[@class='soft-list clearfix']/li/h4/a"
    DOWNLOAD_URL="//div[@class='downLoad-box']/a[@class='downLoad-button androidDown-button']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//h1[@class='soft-title']"
    UPLOAD_TIME="//ul[@class='soft-text']/li[last()]/em"
    CATEGORY="//ul[@class='soft-text']/li[1]/a"
    RATING="//div[@class='rate-box']/em"
    DOWNLOAD_COUNT="//li[@class='item-3']/span[2]"

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
