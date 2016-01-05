# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.downza.cn"
    START_URLS=["http://www.downza.cn/android/yingyong/tppz-576.html","http://www.downza.cn/android/danji/tyjj-386.html","http://www.downza.cn/android/yingyong/yybf-577.html","http://www.downza.cn/android/danji/yzxx-387.html","http://www.downza.cn/android/yingyong/xtrj-578.html","http://www.downza.cn/android/danji/jsby-388.html","http://www.downza.cn/android/yingyong/wltx-579.html","http://www.downza.cn/android/danji/fxsj-389.html","http://www.downza.cn/android/yingyong/shfw-580.html","http://www.downza.cn/android/danji/kpqp-390.html","http://www.downza.cn/android/yingyong/aqfh-581.html","http://www.downza.cn/android/danji/scyx-391.html","http://www.downza.cn/android/yingyong/zxyd-582.html","http://www.downza.cn/android/danji/ycjy-392.html","http://www.downza.cn/android/yingyong/sjqq-583.html","http://www.downza.cn/android/danji/dzyx-393.html","http://www.downza.cn/android/yingyong/sjlt-584.html","http://www.downza.cn/android/danji/yyyx-394.html","http://www.downza.cn/android/yingyong/mvbz-585.html","http://www.downza.cn/android/danji/xgb-395.html","http://www.downza.cn/android/yingyong/dtcx-586.html","http://www.downza.cn/android/danji/cltf-396.html","http://www.downza.cn/android/yingyong/dtbz-587.html","http://www.downza.cn/android/danji/mxjm-397.html","http://www.downza.cn/android/yingyong/qwyl-588.html","http://www.downza.cn/android/danji/etjy-398.html","http://www.downza.cn/android/yingyong/xxlc-589.html","http://www.downza.cn/android/danji/qtyx-399.html","http://www.downza.cn/android/yingyong/swbg-590.html","http://www.downza.cn/android/wangyou/qpyx-401.html","http://www.downza.cn/android/yingyong/ztmh-591.html","http://www.downza.cn/android/wangyou/kpyx-402.html","http://www.downza.cn/android/yingyong/zmkz-592.html","http://www.downza.cn/android/wangyou/hhwy-403.html","http://www.downza.cn/android/yingyong/yxfz-593.html","http://www.downza.cn/android/wangyou/xxyc-404.html","http://www.downza.cn/android/yingyong/jkms-594.html","http://www.downza.cn/android/wangyou/jsby-405.html","http://www.downza.cn/android/wangyou/qtwy-407.html","http://www.downza.cn/android/wangyou/yywd-408.html","http://www.downza.cn/android/wangyou/scjs-409.html","http://www.downza.cn/android/wangyou/xxwy-410.html","http://www.downza.cn/android/wangyou/dzjj-411.html","http://www.downza.cn/android/wangyou/jswy-412.html","http://www.downza.cn/android/wangyou/cltf-413.html","http://www.downza.cn/android/wangyou/tywy-414.html","http://www.downza.cn/android/wangyou/fxsj-415.html","http://www.downza.cn/android/wangyou/sgwy-416.html"]
    DETAIL_URLS="//dd[@class='rmain']/ul/li/a"
    DOWNLOAD_URL="//ul[@class='ul_Address']/li[last()]/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='fixed']/h1"
    UPLOAD_TIME="//div[@class='fixed']/p[3]/i[3]"
    CATEGORY="//p[@class='seat']/a[3]"
    RATING="//div[@class='fixed']/p[3]/i[6]/span"

    def get_upload_time(self,detail_page_driver):
        if self.UPLOAD_TIME is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.UPLOAD_TIME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            upload_time = util.unify_data(ele.text.split("更新：")[1])
        except Exception as e:
            return None
        return upload_time

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("class").split("star")[1])*10)
        except Exception as e:
            return None
        return rating
    
