# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="store.oppomobile.com"
    START_URLS=["http://store.oppomobile.com/product/category/12_6786_1.html","http://store.oppomobile.com/product/category/12_6792_1.html","http://store.oppomobile.com/product/category/12_74_1.html","http://store.oppomobile.com/product/category/12_460_1.html","http://store.oppomobile.com/product/category/12_6762_1.html","http://store.oppomobile.com/product/category/12_6795_1.html","http://store.oppomobile.com/product/category/12_77_1.html","http://store.oppomobile.com/product/category/12_6796_1.html","http://store.oppomobile.com/product/category/12_78_1.html","http://store.oppomobile.com/product/category/12_79_1.html","http://store.oppomobile.com/product/category/12_6761_1.html","http://store.oppomobile.com/product/category/12_80_1.html","http://store.oppomobile.com/product/category/12_463_1.html","http://store.oppomobile.com/product/category/12_462_1.html","http://store.oppomobile.com/product/category/12_465_1.html","http://store.oppomobile.com/product/category/12_81_1.html","http://store.oppomobile.com/product/category/12_85_1.html","http://store.oppomobile.com/product/category/12_469_1.html","http://store.oppomobile.com/product/category/12_82_1.html","http://store.oppomobile.com/product/category/12_1804_1.html","http://store.oppomobile.com/product/category/12_84_1.html","http://store.oppomobile.com/product/category/12_287_1.html","http://store.oppomobile.com/product/category/12_468_1.html"]
    DETAIL_URLS="//div[@class='list_content']/div[@class='li_tubiao']/a[@class='to_xq']"
    DOWNLOAD_URL="//div[@class='soft_info_middle']/a[@class='detail_down']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='soft_info_middle']/h3"
    UPLOAD_TIME="//div[@class='soft_info_middle']/ul[@class='soft_info_more']/li[1]"
    DOWNLOAD_COUNT="//div[@class='soft_info_middle']/div[@class='soft_info_nums']"
    RATING="//div[@class='soft_info_middle']/div[@class='soft_info_nums']/div"
    CATEGORY="//div[@class='bread_nav']/span[3]/a"

    def get_download_count(self,detail_page_driver):
        if self.DOWNLOAD_COUNT is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_COUNT)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            download_count = util.unify_download_count(ele.text.split("评分")[1])
        except Exception as e:
            return None
        return download_count

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("class").split('star_')[1])*2)
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
            downLoadURLID = ele.get_attribute("onclick").split("(")[1].split(")")[0]
            download_url = "http://" + self.SOURCE + "/product/download.html?id=" + downLoadURLID
        except:
            pass
        return download_url
