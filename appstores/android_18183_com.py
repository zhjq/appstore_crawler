# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="android.18183.com"
    START_URLS=["http://android.18183.com/xiazai/wangyou/jsby/","http://android.18183.com/xiazai/wangyou/qpkp/","http://android.18183.com/xiazai/wangyou/xxyz/","http://android.18183.com/xiazai/wangyou/dzcg/","http://android.18183.com/xiazai/wangyou/clzq/","http://android.18183.com/xiazai/wangyou/scjs/","http://android.18183.com/xiazai/wangyou/tyyd/","http://android.18183.com/xiazai/wangyou/sjqz/","http://android.18183.com/xiazai/wangyou/mnjy/","http://android.18183.com/xiazai/wangyou/yywd/","http://android.18183.com/soft/"] 
    DETAIL_URLS="//ul[@class='dow_list']/li/div[3]/a"
    DOWNLOAD_URL="//div[@class='dow_link_h']/ul/li/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//dl[@class='dow_dl']/dd/h1"
    CATEGORY="//dl[@class='dow_dl']/dd/ul/li[1]/i"
    DOWNLOAD_COUNT="//div[@class='num fl']/i"