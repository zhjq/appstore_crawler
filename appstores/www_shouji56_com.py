# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.shouji56.com"
    START_URLS=["http://www.shouji56.com/azsoft/jiaoyou/","http://www.shouji56.com/azsoft/system/","http://www.shouji56.com/azsoft/safe/","http://www.shouji56.com/azsoft/wang/","http://www.shouji56.com/azsoft/tongxun/","http://www.shouji56.com/azsoft/licai/","http://www.shouji56.com/azsoft/xuexi/","http://www.shouji56.com/azsoft/photo/","http://www.shouji56.com/azsoft/daohang/","http://www.shouji56.com/azsoft/life/","http://www.shouji56.com/azsoft/book/","http://www.shouji56.com/azsoft/video/","http://www.shouji56.com/azsoft/meihua/","http://www.shouji56.com/azsoft/music/","http://www.shouji56.com/azsoft/yule/","http://www.shouji56.com/azsoft/liaotian/","http://www.shouji56.com/azgame/gedou/","http://www.shouji56.com/azgame/Race/","http://www.shouji56.com/azgame/mus/http://www.shouji56.com/azgame/sim/","http://www.shouji56.com/azgame/sim/","http://www.shouji56.com/azgame/puz/","http://www.shouji56.com/azgame/sheji/","http://www.shouji56.com/azgame/act/","http://www.shouji56.com/azgame/tafang/","http://www.shouji56.com/azgame/rpg/","http://www.shouji56.com/azgame/kapai/"] 
    DETAIL_URLS="//div[@class='listbox']/div[1]/ul/li/div[2]/a"
    DOWNLOAD_URL="//div[@class='ad_l']/ul[2]/li[last()]/span/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='g_tit']/span"
    CATEGORY="//div[@class='gtext']/ul/li[1]/a"
    UPLOAD_TIME="//div[@class='gtext']/ul/li[5]/span"
    RATING="//span[@id='box_score']"

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.text)*10)
        except Exception as e:
            return None
        return rating
