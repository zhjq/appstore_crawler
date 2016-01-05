# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="soft.4355.com"
    START_URLS=["http://soft.4355.com/shiyonggongju/index.html","http://soft.4355.com/shiwuguanli/","http://soft.4355.com/jiaoyuyuedu/","http://soft.4355.com/duanxinzengqiang/","http://soft.4355.com/zhutizhuomian/","http://soft.4355.com/anquanfanghu/","http://soft.4355.com/shenghuogouwu/","http://soft.4355.com/tonghuafuzhu/","http://soft.4355.com/chaxungongju/","http://soft.4355.com/jiaotongdaohang/","http://soft.4355.com/paizhaosheying/","http://soft.4355.com/yingyinbofang/"]
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
