# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="mm.10086.cn"
    START_URLS=["http://mm.10086.cn/android/game/dzmx?pay=1","http://mm.10086.cn/android/game/fkpk?pay=1","http://mm.10086.cn/android/game/tysc?pay=1","http://mm.10086.cn/android/game/xcyx?pay=1","http://mm.10086.cn/android/game/xxyz?pay=1","http://mm.10086.cn/android/game/sjyx?pay=1","http://mm.10086.cn/android/game/jsby?pay=1","http://mm.10086.cn/android/game/jyyc?pay=1","http://mm.10086.cn/android/game/qpyx?pay=1","http://mm.10086.cn/android/game/clyx?pay=1","http://mm.10086.cn/android/game/etyx?pay=1","http://mm.10086.cn/android/game/wzyx?pay=1","http://mm.10086.cn/android/game/wlyx?pay=1","http://mm.10086.cn/android/game/qtyx?pay=1","http://mm.10086.cn/android/software/srf?pay=1","http://mm.10086.cn/android/software/yygj?pay=1","http://mm.10086.cn/android/software/szyl?pay=1","http://mm.10086.cn/android/software/wlsp?pay=1","http://mm.10086.cn/android/software/cyms?pay=1","http://mm.10086.cn/android/software/sqjy?pay=1","http://mm.10086.cn/android/software/llq?pay=1","http://mm.10086.cn/android/software/mhbz?pay=1","http://mm.10086.cn/android/software/etyy?pay=1","http://mm.10086.cn/android/software/dzsj?pay=1","http://mm.10086.cn/android/software/jkyl?pay=1","http://mm.10086.cn/android/software/ktdm?pay=1","http://mm.10086.cn/android/software/ylbg?pay=1","http://mm.10086.cn/android/software/wlgw?pay=1","http://mm.10086.cn/android/software/sylx?pay=1","http://mm.10086.cn/android/software/aqfh?pay=1","http://mm.10086.cn/android/software/jyjx?pay=1","http://mm.10086.cn/android/software/shzs?pay=1","http://mm.10086.cn/android/software/lycx?pay=1","http://mm.10086.cn/android/software/swbg?pay=1","http://mm.10086.cn/android/software/xtgj?pay=1","http://mm.10086.cn/android/software/thtx?pay=1","http://mm.10086.cn/android/software/bkzz?pay=1","http://mm.10086.cn/android/software/jtdh?pay=1","http://mm.10086.cn/android/software/jrlc?pay=1","http://mm.10086.cn/android/software/xwzx?pay=1"]
    DETAIL_URLS="//div[@class='sequence']/ul/li/div[@class='part-1']/div[@class='info']/a"
    DOWNLOAD_URL="//div[@class='mj_cont']/div[@class='mj_cont_left mj_shadow']/div[@class='mj_cont_left_t']/a[@class='mj_xzdbd']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='mj_big_title font-f-yh']/span"
    CATEGORY="//div[@class='mj_info font-f-yh']/ul/li[6]"
    UPLOAD_TIME="//div[@class='mj_info font-f-yh']/ul/li[7]"

    def get_category(self,detail_page_driver):
        if self.CATEGORY is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.CATEGORY)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            category = ele.text.replace("所属类别：","")
            category = category.replace(" ","")
        except Exception as e:
            return None
        return category