# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.paojiao.cn"
    START_URLS=["http://www.paojiao.cn/wangyou/list_default____1.html"]
    DETAIL_URLS="//div[@class='top-list2']/ul/li/a[2]"
    DOWNLOAD_URL="//a[text()='立即下载']"
    NEXTPAGE="//a[@class='next']"
    APPNAME="//div[@class='app-right']/h2/span"
    UPLOAD_TIME="//div[@id='more_info_context']/p[1]"
    CATEGORY="//div[@id='more_info_context']/p[5]"
    DOWNLOAD_COUNT="//span[@class='item']/i"

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
            download_url = ele.get_attribute("onclick").split("'")[1]
        except Exception:
            pass
        return download_url

    def get_category(self,detail_page_driver):
        if self.CATEGORY is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.CATEGORY)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            category = ele.get_attribute("textContent").strip().split(":")[1].strip()
        except Exception as e:
            return None
        return category

    def get_upload_time(self,detail_page_driver):
        if self.UPLOAD_TIME is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.UPLOAD_TIME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            upload_time = util.unify_data(ele.get_attribute("textContent").strip())
        except Exception as e:
            return None
        return upload_time
