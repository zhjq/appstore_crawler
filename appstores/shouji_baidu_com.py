# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="shouji.baidu.com"
    START_URLS=["http://shouji.baidu.com/software/list?cid=503","http://shouji.baidu.com/game/list?cid=401","http://shouji.baidu.com/software/list?cid=501","http://shouji.baidu.com/game/list?cid=403","http://shouji.baidu.com/software/list?cid=502","http://shouji.baidu.com/game/list?cid=405","http://shouji.baidu.com/software/list?cid=508","http://shouji.baidu.com/game/list?cid=408","http://shouji.baidu.com/software/list?cid=506","http://shouji.baidu.com/game/list?cid=402","http://shouji.baidu.com/software/list?cid=504","http://shouji.baidu.com/game/list?cid=406","http://shouji.baidu.com/software/list?cid=510","http://shouji.baidu.com/game/list?cid=404","http://shouji.baidu.com/software/list?cid=507","http://shouji.baidu.com/game/list?cid=407","http://shouji.baidu.com/software/list?cid=505","http://shouji.baidu.com/software/list?cid=509"]
    DETAIL_URLS="//div[@class='list-bd app-bd']/ul/li/div[@class='app-box']/a"
    DOWNLOAD_URL="//div[@class='area-download']/a[@class='apk']"
    NEXTPAGE="//li[@class='next']/a[text()='>']"
    APPNAME="//h1[@class='app-name']/span"
    CATEGORY="//div[@class='nav']/span[3]/a[1]"
    RATING="//span[@class='star-xbig']/span[@class='star-percent']"
    DOWNLOAD_COUNT="//div[@class='detail']/span[@class='download-num']"


    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("style").split(":")[1].split("%")[0]))
        except Exception as e:
            return None
        return rating

    def get_detail_urls(self,list_page_driver):
        detail_urls = []
        eles = list_page_driver.find_elements_by_xpath(self.DETAIL_URLS)
        if len(eles)==0:
            try:
                list_page_driver.refresh()
            except selenium_exception.TimeoutException as e:
                pass
            eles = list_page_driver.find_elements_by_xpath(self.DETAIL_URLS)
        for ele in eles:
            detail_url = None
            try:
                detail_url = ele.get_attribute('href').split('&from')[0]
            except Exception:
                detail_url = util.href2url(self.SOURCE,ele.get_attribute('href'),util.get_current_url(list_page_driver))
            if detail_url:
                detail_urls.append(detail_url)
        return detail_urls

    def get_detail_page_urls(self):
        for i in xrange(10000000):
            yield 'http://shouji.baidu.com/soft/item?docid='+`i`
