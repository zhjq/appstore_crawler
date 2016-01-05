# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="apk.3310.com"
    START_URLS=["http://apk.3310.com/apps/sjyd/","http://apk.3310.com/apps/bzmh/","http://apk.3310.com/apps/xtaq/","http://apk.3310.com/apps/shsy/","http://apk.3310.com/apps/xxbg/","http://apk.3310.com/apps/yytx/","http://apk.3310.com/apps/wlsq/","http://apk.3310.com/apps/lttx/","http://apk.3310.com/apps/dtdh/","http://apk.3310.com/game/jsmx/","http://apk.3310.com/apps/lcgw/","http://apk.3310.com/apps/qtrj/","http://apk.3310.com/apps/1018/","http://apk.3310.com/apps/1019/","http://apk.3310.com/game/fxsj/","http://apk.3310.com/apps/1020/","http://apk.3310.com/apps/1021/","http://apk.3310.com/game/jyyc/","http://apk.3310.com/apps/1022/","http://apk.3310.com/game/clyx/","http://apk.3310.com/game/tyjs/","http://apk.3310.com/game/kpqp/","http://apk.3310.com/game/xxyz/","http://apk.3310.com/game/dzgd/","http://apk.3310.com/game/680/","http://apk.3310.com/game/qtyx/","http://apk.3310.com/game/1023/"]
    DETAIL_URLS="//div[@id='SoftListBox']/ul/li/a"
    DOWNLOAD_URL="//div[@class='pos']/div[@class='btn']/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='cont']/h2"
    CATEGORY="//div[@class='guide']/a[4]"
    RATING="//div[@class='score']/span"
    UPLOAD_TIME="//div[@class='cont']/p[2]"
    DOWNLOAD_COUNT="//div[@class='cont']/p[1]/span[@id='downnum']"

    def get_rating(self,detail_page_driver):
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.text)*20)
        except Exception as e:
            return None
        return rating
