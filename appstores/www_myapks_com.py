# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.myapks.com"
    START_URLS=["http://www.myapks.com/soft/shejiaoweibo","http://www.myapks.com/soft/xitongruanjian","http://www.myapks.com/soft/bangongruanjian","http://www.myapks.com/soft/yueduruanjian","http://www.myapks.com/soft/wangluoruanjian","http://www.myapks.com/soft/anquanruanjian","http://www.myapks.com/soft/tongxinruanjian","http://www.myapks.com/soft/zhuomianruanjian","http://www.myapks.com/soft/yingyinruanjian","http://www.myapks.com/soft/tuxiangruanjian","http://www.myapks.com/soft/chaxunruanjian","http://www.myapks.com/soft/shenghuoruanjian","http://www.myapks.com/soft/shururuanjian","http://www.myapks.com/soft/soft/xuexiruanjian","http://www.myapks.com/soft/qitaruanjian","http://www.myapks.com/game/danjiyouxi/feixingyouxi","http://www.myapks.com/game/danjiyouxi/jiaosebanyan","http://www.myapks.com/game/danjiyouxi/dongzuoyouxi","http://www.myapks.com/game/danjiyouxi/yizhixiuxian","http://www.myapks.com/game/danjiyouxi/jishizhanlue","http://www.myapks.com/game/danjiyouxi/maoxianyouxi","http://www.myapks.com/game/danjiyouxi/qipaiyouxi","http://www.myapks.com/game/danjiyouxi/tiyuyouxi","http://www.myapks.com/game/danjiyouxi/celueyouxi","http://www.myapks.com/game/danjiyouxi/yinyueyouxi","http://www.myapks.com/game/danjiyouxi/monijingying","http://www.myapks.com/game/danjiyouxi/qitayouxi","http://www.myapks.com/game/danjiyouxi/gedouyouxi","http://www.myapks.com/game/danjiyouxi/jingsuyouxi","http://www.myapks.com/game/danjiyouxi/shejiyouxi","http://www.myapks.com/game/shoujiwangyou"]
    DETAIL_URLS="//div[@class='list-game']/div[@class='con']/p[@class='sp1']/a"
    DOWNLOAD_URL="//div[@class='pop-game']/div[@class='con']/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='dl-game fl']/div[@class='con']/h1[@class='tit']/a"
    CATEGORY="//dl[@class='dl-info fl']/dd[3]/a"
    DOWNLOAD_COUNT="//dl[@class='dl-info fl']/dd[1]"
    UPLOAD_TIME="//dl[@class='dl-info fl']/dd[4]"

