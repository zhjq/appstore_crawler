# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="android.gamedog.cn"
    START_URLS=["http://android.gamedog.cn/list_theme_0_581_0_0_0_0.html","http://android.gamedog.cn/list_theme_0_575_0_0_0_0.html","http://android.gamedog.cn/list_theme_0_193_0_0_0_0.html","http://android.gamedog.cn/list_theme_0_192_0_0_0_0.html","http://android.gamedog.cn/list_theme_0_191_0_0_0_0.html","http://android.gamedog.cn/list_theme_0_190_0_0_0_0.html","http://android.gamedog.cn/list_theme_0_189_0_0_0_0.html","http://android.gamedog.cn/list_theme_0_188_0_0_0_0.html","http://android.gamedog.cn/list_theme_0_187_0_0_0_0.html","http://android.gamedog.cn/list_theme_0_186_0_0_0_0.html","http://android.gamedog.cn/list_theme_0_185_0_0_0_0.html","http://android.gamedog.cn/list_theme_0_184_0_0_0_0.html","http://android.gamedog.cn/list_theme_0_183_0_0_0_0.html","http://android.gamedog.cn/list_theme_0_182_0_0_0_0.html","http://android.gamedog.cn/list_theme_0_181_0_0_0_0.html","http://android.gamedog.cn/list_theme_0_180_0_0_0_0.html","http://android.gamedog.cn/list_theme_0_194_0_0_0_0.html","http://android.gamedog.cn/list_theme_0_195_0_0_0_0.html"]
    DETAIL_URLS="//ul[@class='theme_list']/li/a"
    DOWNLOAD_URL="//a[@class='p-downs']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='bz_info']/ul/li[1]/span"
    UPLOAD_TIME="//div[@class='bz_info']/ul/li[2]/span[1]"
    CATEGORY="//div[@class='bz_info']/ul/li[5]"
    RATING="//div[@class='bz_info']/ul/li[3]/img"
    DOWNLOAD_COUNT="//div[@class='bz_info']/ul/li[4]/span"

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("src").split("star")[1].split(".")[0])*20)
        except Exception as e:
            return None
        return rating

    def get_category(self,detail_page_driver):
        if self.CATEGORY is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.CATEGORY)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            category = ele.text.split("：")[1]
            category = category + "主题"
        except Exception as e:
            return None
        return category