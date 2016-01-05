# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.anzhuoapk.com"
    START_URLS=["http://www.anzhuoapk.com/apps-25-1/","http://www.anzhuoapk.com/apps-13-1/","http://www.anzhuoapk.com/apps-6-1/","http://www.anzhuoapk.com/apps-7-1/","http://www.anzhuoapk.com/apps-37-1/","http://www.anzhuoapk.com/apps-355-1/","http://www.anzhuoapk.com/apps-33-1/","http://www.anzhuoapk.com/apps-36-1/","http://www.anzhuoapk.com/apps-11-1/","http://www.anzhuoapk.com/apps-35-1/","http://www.anzhuoapk.com/apps-34-1/","http://www.anzhuoapk.com/apps-117-1/","http://www.anzhuoapk.com/apps-83-1/","http://www.anzhuoapk.com/apps-391-1/","http://www.anzhuoapk.com/games-23-2/","http://www.anzhuoapk.com/games-19-2/","http://www.anzhuoapk.com/games-20-2/","http://www.anzhuoapk.com/games-131-2/","http://www.anzhuoapk.com/games-15-2/","http://www.anzhuoapk.com/games-16-2/","http://www.anzhuoapk.com/games-21-2/","http://www.anzhuoapk.com/games-139-2/"]
    DETAIL_URLS="//div[@class='app_all_list']/dl/dd/div[@class='app_txt z']/p/a"
    DOWNLOAD_URL="//div[@class='content1_bottom']/a[1]"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='content1_top_txt z']/h1"
    UPLOAD_TIME="//div[@class='ctxt']/span[5]"
    CATEGORY="//div[@class='position']/a[3]"
    DOWNLOAD_COUNT="//div[@class='ctxt']/span[3]"
    RATING="//p[@class='app_level']/span"

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("class").split("star")[1].split(" ")[0])*10)
        except Exception as e:
            return None
        return rating
