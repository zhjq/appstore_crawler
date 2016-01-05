# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="d.4355.com"
    START_URLS=["http://d.4355.com/jiaosebanyan/","http://d.4355.com/dongzuoyouxi/","http://d.4355.com/maoxianyouxi/","http://d.4355.com/tiyuyouxi/","http://d.4355.com/xiuxianyizhi/","http://d.4355.com/qipaiyouxi/","http://d.4355.com/monijingying/","http://d.4355.com/saichejingsu/","http://d.4355.com/shejiyouxi/","http://d.4355.com/zhanlueyouxi/","http://d.4355.com/wangluoyouxi/","http://d.4355.com/qitayouxi/"]
    DETAIL_URLS="//div[@class='downlist boxbg lazy clearfix']/ul/li/div/b/a"
    DOWNLOAD_URL="//ul[@class='clearfix']/li/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='gameinfo']/h1"
    CATEGORY="//div[@class='location']/a[3]"
    RATING="//b[@id='pfenshowdiv']"
    UPLOAD_TIME="//div[@class='gameinfo']/ul/li[6]"
    DOWNLOAD_COUNT="//div[@class='gameinfo']/ul/li[3]/i"
    
    def get_rating(self,detail_page_driver):
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.text)*10)
        except Exception as e:
            return None
        return rating
