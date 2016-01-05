# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="a.3533.com"
    START_URLS=["http://a.3533.com/ruanjian/1/","http://a.3533.com/ruanjian/2/","http://a.3533.com/ruanjian/3/","http://a.3533.com/ruanjian/4/","http://a.3533.com/ruanjian/5/","http://a.3533.com/ruanjian/6/","http://a.3533.com/ruanjian/7/","http://a.3533.com/ruanjian/8/","http://a.3533.com/wangyou/","http://a.3533.com/youxi/2/","http://a.3533.com/youxi/3/","http://a.3533.com/youxi/4/","http://a.3533.com/youxi/5/","http://a.3533.com/youxi/6/","http://a.3533.com/youxi/7/","http://a.3533.com/youxi/8/","http://a.3533.com/youxi/9/","http://a.3533.com/youxi/10/","http://a.3533.com/youxi/11/","http://a.3533.com/youxi/12/","http://a.3533.com/youxi/13/","http://a.3533.com/youxi/14/","http://a.3533.com/youxi/15/"]
    DETAIL_URLS="//div[@class='module list']/div[@class='bd']/ul/li/a[2]"
    DOWNLOAD_URL="//div[@class='download']/a"
    CHECKMORE="//div[@class='module more']/div/a"
    APPNAME="//h1[@class='title']"
    CATEGORY="//div[@class='breadcrumb']/a[4]/span"