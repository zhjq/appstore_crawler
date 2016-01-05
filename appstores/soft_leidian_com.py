# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="soft.leidian.com"
    START_URLS=["http://soft.leidian.com/list/index/cid/11/size/all/order/download/","http://soft.leidian.com/list/index/cid/12/size/all/order/download/","http://soft.leidian.com/list/index/cid/13/size/all/order/download/","http://soft.leidian.com/list/index/cid/14/size/all/order/download/","http://soft.leidian.com/list/index/cid/15/size/all/order/download/","http://soft.leidian.com/list/index/cid/16/size/all/order/download/","http://soft.leidian.com/list/index/cid/17/size/all/order/download/","http://soft.leidian.com/list/index/cid/18/size/all/order/download/"]
    DETAIL_URLS="//div[@id='doc']/div[@id='bd']/div[@class='app-box']/div[@id='js-tab']/div[@class='bd js-views']/div[@class='mod-pro-list']/ul/li/h4/a"
    DOWNLOAD_URL="//div[@class='col9 first']/div[@class='mod-soft-info clearfix']/div[@class='options']/div[@class='setupextra']/a"
    NEXTPAGE="//li[@title='下一页']/a"
    APPNAME="//div[@class='soft-bc-info clearfix']/h1"
    CATEGORY="//div[@id='doc']/div[@id='bd']/div[@class='crumb']/a[2]"
    UPLOAD_TIME="//div[@class='intro']/div[@class='soft-extra-info']/span[@class='update-time']"
    DOWNLOAD_COUNT="//div[@class='intro']/div[@class='soft-extra-info']/span[@class='dl-cnt']"

    def get_rating(self,detail_page_driver):
        rating = None
        try:
            score_int = detail_page_driver.find_element_by_xpath("//div[@class='mod-rate']/span[@class='int']").text
            score_decimal = detail_page_driver.find_element_by_xpath("//div[@class='mod-rate']/span[@class='decimal']").text
            rating = float(int(score_int)*10 + int(score_decimal))
        except Exception as e:
            return None
        return rating