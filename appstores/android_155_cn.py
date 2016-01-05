# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="android.155.cn"
    START_URLS=["http://android.155.cn/game/rpg.html","http://android.155.cn/game/act.html","http://android.155.cn/game/spt.html","http://android.155.cn/game/sht.html","http://android.155.cn/game/slg.html","http://android.155.cn/game/lsr.html","http://android.155.cn/game/wsd.html","http://android.155.cn/game/cct.html","http://android.155.cn/game/avt.html","http://android.155.cn/game/oth.html","http://android.155.cn/game/sim.html"]   
    DETAIL_URLS="//div[@class='sof_r_center']/div/dl/dt/a"
    DOWNLOAD_URL="//div[@class='bottom_down']/a"
    NEXTPAGE="//a[text()='下页']"
    APPNAME="//div[@class='left_icon']/h1"
    CATEGORY="//div[@class='xinxi_center']/p[1]"
    UPLOAD_TIME="//div[@class='xinxi_center']/p[7]/span"
    DOWNLOAD_COUNT="//div[@class='xinxi_center']/p[4]/span"