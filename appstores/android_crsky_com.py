# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="android.crsky.com"
    START_URLS=["http://android.crsky.com/app/liaotiantongxun.html","http://android.crsky.com/app/xitonggongju.html","http://android.crsky.com/app/wangluoliulan.html","http://android.crsky.com/app/anquanshadu.html","http://android.crsky.com/app/shurufa.html","http://android.crsky.com/app/shoujiyuedu.html","http://android.crsky.com/app/bofangqi.html","http://android.crsky.com/app/ditudaohang.html","http://android.crsky.com/app/gupiaozhengquan.html","http://android.crsky.com/app/paizhaotuxiang.html","http://android.crsky.com/app/xinwenzixun.html","http://android.crsky.com/app/bangongkaoshi.html","http://android.crsky.com/app/bianjieshenghuo.html","http://android.crsky.com/app/wangluoshejiao.html","http://android.crsky.com/app/wanggouzhifu.html","http://android.crsky.com/app/qitaruanjian.html","http://android.crsky.com/game/fxsj.html","http://android.crsky.com/game/yzxx.html","http://android.crsky.com/game/dzyx.html","http://android.crsky.com/game/scyx.html","http://android.crsky.com/game/jsby.html","http://android.crsky.com/game/gdyx.html","http://android.crsky.com/game/tfyx.html","http://android.crsky.com/game/wlyx.html","http://android.crsky.com/game/tyjj.html","http://android.crsky.com/game/qpyx.html","http://android.crsky.com/game/qtyx.html"]
    DETAIL_URLS="//div[@class='right']/p/a"
    DOWNLOAD_URL="//a[text()='联通网通下载点']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='soft_news']/div[@class='left']/div[@class='s_line'][1]/p/span"
    CATEGORY="//div[@class='soft_news']/div[@class='left']/div[@class='s_line'][3]/p[1]/span"
    RATING="//div[@class='tuij']/img"
    DOWNLOAD_COUNT="//div[@class='soft_news']/div[@class='left']/div[@class='s_line'][3]/p[2]/span"

    def get_rating(self,detail_page_driver):
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("src").split('images/')[1].split('star')[0])*20)
        except Exception as e:
            return None
        return rating
