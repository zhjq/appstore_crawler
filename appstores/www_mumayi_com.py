# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.mumayi.com"
    START_URLS=["http://www.mumayi.com/android/xitonggongju/","http://www.mumayi.com/android/zhutibizhi/","http://www.mumayi.com/android/wangluoliulan/","http://www.mumayi.com/android/jishitongxun/","http://www.mumayi.com/android/shejiaoweibo/","http://www.mumayi.com/android/yinyueshipin/","http://www.mumayi.com/android/sheyingtuxiang/","http://www.mumayi.com/android/tianqishijian/","http://www.mumayi.com/android/anquanshadu/","http://www.mumayi.com/android/xinwenzixun/","http://www.mumayi.com/android/tonghuazengqiang/","http://www.mumayi.com/android/duanxinzengqiang/","http://www.mumayi.com/android/bianjieshenghuo/","http://www.mumayi.com/android/chuxingditu/","http://www.mumayi.com/android/gouwulicia/","http://www.mumayi.com/android/jiaoyuxuexi/","http://www.mumayi.com/android/shangwubangong/","http://www.mumayi.com/android/yiliaobaojian/","http://www.mumayi.com/android/xiuxianyule/","http://www.mumayi.com/android/tushudongman/","http://www.mumayi.com/android/juesebanyan/","http://www.mumayi.com/android/feixingyouxi/","http://www.mumayi.com/android/tiyujinji/","http://www.mumayi.com/android/yizixiuxian/","http://www.mumayi.com/android/qipaitiandi/","http://www.mumayi.com/android/saicheyouxi/","http://www.mumayi.com/android/dongzuoyouxi/","http://www.mumayi.com/android/yangchengyouxi/","http://www.mumayi.com/android/youximoni/","http://www.mumayi.com/android/qitayouxi/"]
    DETAIL_URLS="//ul[@class='androidList clearf block ']/li/a[2]"
    DOWNLOAD_URL="//div[@class='ibtn fl']/a[@class='download fl']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//h1[@class='iappname hidden fl']"
    UPLOAD_TIME="//ul[@class='istyle fl']/li[3]"
    DOWNLOAD_COUNT="//div[@class='ibtn fl']/a[@class='download fl']/i[3]/span"
    RATING="//li[@class='isli stars']/div[@id='starlist']"
    CATEGORY="//ul[@class='istyle fl']/li[2]"


    def get_rating(self,detail_page_driver):
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("class").split("now")[1])*2)
        except Exception as e:
            return None
        return rating
