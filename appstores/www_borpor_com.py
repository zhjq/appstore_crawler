# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.borpor.com"
    START_URLS=["http://www.borpor.com/class.php?ctype=d&cid=2","http://www.borpor.com/class.php?ctype=d&cid=3","http://www.borpor.com/class.php?ctype=d&cid=4","http://www.borpor.com/class.php?ctype=d&cid=5","http://www.borpor.com/class.php?ctype=d&cid=6","http://www.borpor.com/class.php?ctype=d&cid=63","http://www.borpor.com/class.php?ctype=d&cid=76"]
    DETAIL_URLS="//p[@class='STYLE2']/a"
    DOWNLOAD_URL="//div[@id='popup']/div/a[@id='dow360']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//li[@class='xay']"
    CATEGORY="//li[@class='sidebar']/a[3]"
    UPLOAD_TIME="//table[@class='f-11-b3b3b3']/tbody/tr[6]/td[2]"
    RATING="//table[@class='f-11-b3b3b3']/tbody/tr[1]/td[2]"

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("class").split("star")[2])*20)
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
            downLoadURLID = ele.get_attribute("href").split("=")[1].split("#")[0]
            download_url = "http://www.borpor.com/download.php?gid=" + downLoadURLID
        except Exception:
            pass
        return download_url
