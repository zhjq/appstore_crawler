# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="game.leidian.com"
    START_URLS=["http://game.leidian.com/list/index/cid/101587/size/all/order/download/","http://game.leidian.com/list/index/cid/19/size/all/order/download/","http://game.leidian.com/list/index/cid/20/size/all/order/download/","http://game.leidian.com/list/index/cid/100451/size/all/order/download/","http://game.leidian.com/list/index/cid/51/size/all/order/download/","http://game.leidian.com/list/index/cid/52/size/all/order/download/","http://game.leidian.com/list/index/cid/53/size/all/order/download/","http://game.leidian.com/list/index/cid/54/size/all/order/download/"]
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