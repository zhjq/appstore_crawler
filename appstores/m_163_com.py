# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="m.163.com"
    START_URLS=["http://m.163.com/android/category/ca8mth20dq/index.html","http://m.163.com/android/category/ca8mth2ec5/index.html","http://m.163.com/android/category/ca8n2dr6he/index.html","http://m.163.com/android/category/ca8mth1d1v/index.html","http://m.163.com/android/category/ca8mth2h9n/index.html","http://m.163.com/android/category/ca8mtgvp7p/index.html","http://m.163.com/android/category/ca8mth056g/index.html","http://m.163.com/android/category/ca8mth1irk/index.html","http://m.163.com/android/category/ca8mth0kq4/index.html","http://m.163.com/android/category/ca8mth102m/index.html","http://m.163.com/android/category/ca8mth0278/index.html","http://m.163.com/android/category/ca8nek7jpg/index.html","http://m.163.com/android/category/ca8nek8hfr/index.html","http://m.163.com/android/category/ca8mth1g53/index.html","http://m.163.com/android/category/ca8mth1tc0/index.html","http://m.163.com/android/category/ca8mtgvh2s/index.html","http://m.163.com/android/category/ca8mth23e7/index.html","http://m.163.com/android/category/ca8mtggn3j/index.html","http://m.163.com/android/category/ca8mtgvddb/index.html","http://m.163.com/android/game/ca96b6hqnd/index.html","http://m.163.com/android/game/ca9a2rrf59/index.html","http://m.163.com/android/game/ca9a2rseok/index.html","http://m.163.com/android/game/ca96b6i1vh/index.html","http://m.163.com/android/game/ca96b6icj1/index.html","http://m.163.com/android/game/ca96b6j8hh/index.html","http://m.163.com/android/game/ca9a2ruhh3/index.html","http://m.163.com/android/game/ca9a2ruhh3/index.html","http://m.163.com/android/game/cabv42qn7s/index.html"]
    DETAIL_URLS="//div[@class='arti-bd']/div[@class='arti-bd-content']/div[@id='appsview']/div[@class='yui3-appsview-list']/ul/li/div/div/div[@class='apps-info-text']/div/p[@class='f-s3 t-overflow']/a"
    DOWNLOAD_URL="//div[@class='clearfix']/div[@class='sect-side-s']/div/p[@class='m-t15']/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//span[@class='f-h1']"
    RATING="//div[@class='m-t5 clearfix']/div[@class='fl-l m-r15']/span/i"
    CATEGORY="//div[@class='sect']/div[@class='crumb']/a[3]"

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
