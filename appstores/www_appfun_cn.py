# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.appfun.cn"
    START_URLS=["http://www.appfun.cn/soft/applist/cid/9","http://www.appfun.cn/soft/applist/cid/10","http://www.appfun.cn/soft/applist/cid/11","http://www.appfun.cn/soft/applist/cid/12","http://www.appfun.cn/soft/applist/cid/13","http://www.appfun.cn/soft/applist/cid/14","http://www.appfun.cn/soft/applist/cid/15","http://www.appfun.cn/soft/applist/cid/16","http://www.appfun.cn/soft/applist/cid/17","http://www.appfun.cn/soft/applist/cid/18","http://www.appfun.cn/soft/applist/cid/19","http://www.appfun.cn/soft/applist/cid/20","http://www.appfun.cn/soft/applist/cid/21","http://www.appfun.cn/soft/applist/cid/22","http://www.appfun.cn/soft/applist/cid/23","http://www.appfun.cn/soft/applist/cid/24","http://www.appfun.cn/soft/applist/cid/25","http://www.appfun.cn/soft/applist/cid/26","http://www.appfun.cn/soft/applist/cid/27","http://www.appfun.cn/soft/applist/cid/28","http://www.appfun.cn/game/applist/cid/2","http://www.appfun.cn/game/applist/cid/3","http://www.appfun.cn/game/applist/cid/4","http://www.appfun.cn/game/applist/cid/5","http://www.appfun.cn/game/applist/cid/6","http://www.appfun.cn/game/applist/cid/7","http://www.appfun.cn/game/applist/cid/8"]
    DETAIL_URLS="//div[@class='app-max']/div[@class='app-detail']/h4/a"
    DOWNLOAD_URL="//div[@class='content-detailCtn-icon']/a"
    NEXTPAGE="//a[text()='下一页»']"
    APPNAME="//div[@class='content-categoryCtn-title clearfix']/h1"
    CATEGORY="//ul[@class='sideBar-appDetail']/li[1]/div/a"
    UPLOAD_TIME="//ul[@class='sideBar-appDetail']/li[4]/div"
