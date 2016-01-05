# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception
import time

class Store(Base):
    SOURCE="dl.pconline.com.cn"
    START_URLS=["http://dl.pconline.com.cn/sort/1453.html","http://dl.pconline.com.cn/sort/1466.html","http://dl.pconline.com.cn/sort/1454.html","http://dl.pconline.com.cn/sort/1467.html","http://dl.pconline.com.cn/sort/1455.html","http://dl.pconline.com.cn/sort/1468.html","http://dl.pconline.com.cn/sort/1456.html","http://dl.pconline.com.cn/sort/1469.html","http://dl.pconline.com.cn/sort/1457.html","http://dl.pconline.com.cn/sort/1470.html","http://dl.pconline.com.cn/sort/1458.html","http://dl.pconline.com.cn/sort/1459.html","http://dl.pconline.com.cn/sort/1471.html","http://dl.pconline.com.cn/sort/1460.html","http://dl.pconline.com.cn/sort/1461.html","http://dl.pconline.com.cn/sort/1462.html","http://dl.pconline.com.cn/sort/1463.html","http://dl.pconline.com.cn/sort/1464.html","http://dl.pconline.com.cn/sort/1465.html","http://dl.pconline.com.cn/sort/1491.html","http://dl.pconline.com.cn/sort/1472.html"]
    DETAIL_URLS="//ul[@class='list']/li/div[@class='listCon']/div[@class='lcTop clearfix']/strong/a"
    DOWNLOAD_URL="//a[@id='linkPage']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//span[@class='mark']/h1"
    UPLOAD_TIME="//div[@class='megs']/div[@class='megR']/ul/li[2]/i[2]/span[3]"
    CATEGORY="//div[@class='wrap clearfix artWrap']/div[@class='guide']/i[@class='fl']/a[5]"
    RATING="//div[@class='megs']/div[@class='megR']/ul/li[3]/i[1]/span[2]/a/em"
    DOWNLOAD_COUNT="//div[@class='dlLink']/div[@class='megL']/a[@id='linkPage']/em"

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("style").split(" ")[1].split("%")[0]))
        except Exception as e:
            return None
        return rating

    def get_download_url(self,detail_page_driver):
        time.sleep(1.5)
        download_url = None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_URL)
        except selenium_exception.NoSuchElementException as e:
            try:
                detail_page_driver.refresh()
            except selenium_exception.TimeoutException as e:
                pass
            try:
                ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_URL)
            except selenium_exception.NoSuchElementException as e:
                return download_url
        return util.href2url(self.SOURCE,ele.get_attribute('href'),util.get_current_url(detail_page_driver))
