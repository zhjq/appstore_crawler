# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.7yw.cn"
    START_URLS=["http://www.7yw.cn/game/new/2","http://www.7yw.cn/game/new/3","http://www.7yw.cn/game/new/4","http://www.7yw.cn/game/new/5","http://www.7yw.cn/game/new/6","http://www.7yw.cn/game/new/7","http://www.7yw.cn/game/new/8","http://www.7yw.cn/game/new/9","http://www.7yw.cn/game/new/10","http://www.7yw.cn/game/new/11","http://www.7yw.cn/game/new/12","http://www.7yw.cn/game/new/13","http://www.7yw.cn/game/new/14","http://www.7yw.cn/game/new/15","http://www.7yw.cn/game/new/16","http://www.7yw.cn/game/new/17","http://www.7yw.cn/game/new/20","http://www.7yw.cn/game/new/47","http://www.7yw.cn/game/new/48","http://www.7yw.cn/game/new/50","http://www.7yw.cn/olgame"]
    DETAIL_URLS="//div[@class='fplist']/div/div[2]/div/a"
    DOWNLOAD_URL="//a[text()='本地下载']"
    NEXTPAGE="//a[text()='下页']"
    APPNAME="//div[@class='nrytitle']/h1"
    UPLOAD_TIME="//div[@class='xiangxi1']/p[2]"
    CATEGORY="//div[@class='xiangxi1']/p[1]"