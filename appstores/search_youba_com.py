# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="search.youba.com"
    START_URLS=["http://search.youba.com/zhaoyouxi/?order=new&platform=1&gameTag=1343","http://search.youba.com/zhaoyouxi/?order=new&platform=1&gameTag=1351","http://search.youba.com/zhaoyouxi/?order=new&platform=1&gameTag=1349","http://search.youba.com/zhaoyouxi/?order=new&platform=1&gameTag=1350","http://search.youba.com/zhaoyouxi/?order=new&platform=1&gameTag=1352","http://search.youba.com/zhaoyouxi/?order=new&platform=1&gameTag=1346","http://search.youba.com/zhaoyouxi/?order=new&platform=1&gameTag=1347","http://search.youba.com/zhaoyouxi/?order=new&platform=1&gameTag=1344","http://search.youba.com/zhaoyouxi/?order=new&platform=1&gameTag=1348","http://search.youba.com/zhaoyouxi/?order=new&platform=1&gameTag=1356","http://search.youba.com/zhaoyouxi/?order=new&platform=1&gameTag=1353","http://search.youba.com/zhaoyouxi/?order=new&platform=1&gameTag=1357","http://search.youba.com/zhaoyouxi/?order=new&platform=1&gameTag=1354","http://search.youba.com/zhaoyouxi/?order=new&platform=1&gameTag=1358","http://search.youba.com/zhaoyouxi/?order=new&platform=1&gameTag=1355"] 
    DETAIL_URLS="//div[@class='main-list']/div/div[2]/a"
    DOWNLOAD_URL="//li[@class='android']/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='app']/div[1]/h1"
    CATEGORY="//p[@class='tag']/span[2]/a[1]"
    RATING="//div[@class='subtitle']/span[2]"

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
