# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.muzhiwan.com"
    START_URLS=["http://www.muzhiwan.com/category/6/","http://www.muzhiwan.com/category/16/","http://www.muzhiwan.com/category/9/","http://www.muzhiwan.com/category/14/","http://www.muzhiwan.com/category/17/","http://www.muzhiwan.com/category/18/","http://www.muzhiwan.com/category/19/"]
    DETAIL_URLS="//ul[@class='gamelist pt10 pb20 pl10']/li/div/a"
    DOWNLOAD_URL="//div[@class='detail_dbtn detail_way_t']/a[@class='local']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='game_name']/h1"
    CATEGORY="//div[@class='bread_Nav']/a[2]"
    UPLOAD_TIME="//div[@class='detail_info']/div[@class='clearfix']/ul/li[5]"
    DOWNLOAD_COUNT="//div[@class='detail_info']/div[@class='clearfix']/ul/li[4]/span[@id='downCount']"
