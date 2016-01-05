# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.apk3.com"
    START_URLS=["http://www.apk3.com/List/1-1.html","http://www.apk3.com/List/3-1.html","http://www.apk3.com/List/2-1.html","http://www.apk3.com/List/4-1.html","http://www.apk3.com/List/5-1.html","http://www.apk3.com/List/6-1.html","http://www.apk3.com/List/47-1.html","http://www.apk3.com/List/67-1.html","http://www.apk3.com/List/68-1.html","http://www.apk3.com/List/107-1.html","http://www.apk3.com/List/79-1.html","http://www.apk3.com/List/80-1.html","http://www.apk3.com/List/81-1.html","http://www.apk3.com/List/82-1.html","http://www.apk3.com/List/83-1.html","http://www.apk3.com/List/84-1.html","http://www.apk3.com/List/85-1.html","http://www.apk3.com/List/86-1.html","http://www.apk3.com/List/87-1.html","http://www.apk3.com/List/88-1.html","http://www.apk3.com/List/89-1.html","http://www.apk3.com/List/90-1.html"]
    DETAIL_URLS="//div[@class='l_app_list']/ul/li/strong/a"
    DOWNLOAD_URL="//div[@class='w320 l a_app_downlist']/ul[1]/li[1]/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='a_app_attr_tit']/h1"
    CATEGORY="//div[@class='wrap']/a[3]"
    DOWNLOAD_COUNT="//div[@class='a_app_attr r']/p[1]/span"
    UPLOAD_TIME="//div[@class='a_app_attr r']/p[1]"

    def get_upload_time(self,detail_page_driver):
        if self.UPLOAD_TIME is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.UPLOAD_TIME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            upload_time = util.unify_data(ele.text.split("：")[4])
        except Exception as e:
            return None
        return upload_time
