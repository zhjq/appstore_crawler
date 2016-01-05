# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="a.3533.com"
    START_URLS=["http://a.3533.com/bizhi/11/","http://a.3533.com/bizhi/1/","http://a.3533.com/bizhi/2/","http://a.3533.com/bizhi/3/","http://a.3533.com/bizhi/5/","http://a.3533.com/bizhi/6/","http://a.3533.com/bizhi/7/","http://a.3533.com/bizhi/8/","http://a.3533.com/bizhi/9/","http://a.3533.com/bizhi/10/","http://a.3533.com/bizhi/12/","http://a.3533.com/bizhi/13/","http://a.3533.com/bizhi/14/","http://a.3533.com/bizhi/15/"]
    DETAIL_URLS="//div[@class='module list']/div[@class='bd']/ul/li/a[2]"
    DOWNLOAD_URL="//div[@class='download']/a"
    CHECKMORE="//div[@class='module more']/div/a"
    APPNAME="//h1[@class='title']"
    RATING="//div[@class='module paper']/div/div[@class='info']/div"
    CATEGORY="//div[@class='breadcrumb']/a[4]/span"

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