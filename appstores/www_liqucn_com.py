# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.liqucn.com"
    START_URLS=["http://www.liqucn.com/rj/c/258/","http://www.liqucn.com/rj/c/243/","http://www.liqucn.com/rj/c/242/","http://www.liqucn.com/rj/c/202/","http://www.liqucn.com/rj/c/277/","http://www.liqucn.com/rj/c/278/","http://www.liqucn.com/rj/c/279/","http://www.liqucn.com/rj/c/280/","http://www.liqucn.com/rj/c/285/","http://www.liqucn.com/rj/c/286/","http://www.liqucn.com/rj/c/288/","http://www.liqucn.com/rj/c/290/","http://www.liqucn.com/rj/c/291/","http://www.liqucn.com/rj/c/293/","http://www.liqucn.com/rj/c/294/","http://www.liqucn.com/rj/c/297/","http://www.liqucn.com/rj/c/298/","http://www.liqucn.com/rj/c/302/","http://www.liqucn.com/rj/c/307/","http://www.liqucn.com/rj/c/310/","http://www.liqucn.com/rj/c/312/","http://www.liqucn.com/rj/c/313/","http://www.liqucn.com/rj/c/394/","http://www.liqucn.com/yx/c/341/","http://www.liqucn.com/yx/c/327/","http://www.liqucn.com/yx/c/328/","http://www.liqucn.com/yx/c/329/","http://www.liqucn.com/yx/c/331/","http://www.liqucn.com/yx/c/339/","http://www.liqucn.com/yx/c/333/","http://www.liqucn.com/yx/c/334/","http://www.liqucn.com/yx/c/335/","http://www.liqucn.com/yx/c/336/","http://www.liqucn.com/yx/c/337/","http://www.liqucn.com/yx/c/343/","http://www.liqucn.com/yx/c/1579/"]
    DETAIL_URLS="//ul[@class='app_list']/li/div[@class='app_name']/a"
    DOWNLOAD_URL="//div[@class='version_down']/div[1]/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='app_leftinfo']/h1"
    CATEGORY="//div[@class='box']/p[@class='pos']/a[3]"
    UPLOAD_TIME="//div[@class='app_leftinfo']/p[1]/em[2]"
