# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="app.suning.com"
    START_URLS=["http://app.suning.com/android/app?gid=1&cid=66","http://app.suning.com/android/app?gid=1&cid=67","http://app.suning.com/android/app?gid=1&cid=182","http://app.suning.com/android/app?gid=1&cid=63","http://app.suning.com/android/app?gid=1&cid=69","http://app.suning.com/android/app?gid=1&cid=72","http://app.suning.com/android/app?gid=1&cid=73","http://app.suning.com/android/app?gid=1&cid=88","http://app.suning.com/android/app?gid=1&cid=76","http://app.suning.com/android/app?gid=1&cid=181","http://app.suning.com/android/app?gid=1&cid=75","http://app.suning.com/android/app?gid=1&cid=189","http://app.suning.com/android/app?gid=1&cid=64","http://app.suning.com/android/app?gid=1&cid=71","http://app.suning.com/android/app?gid=1&cid=78","http://app.suning.com/android/app?gid=1&cid=180","http://app.suning.com/android/app?gid=4&cid=184","http://app.suning.com/android/app?gid=4&cid=191","http://app.suning.com/android/app?gid=4&cid=21","http://app.suning.com/android/app?gid=4&cid=183","http://app.suning.com/android/app?gid=4&cid=22","http://app.suning.com/android/app?gid=4&cid=185","http://app.suning.com/android/app?gid=4&cid=190","http://app.suning.com/android/app?gid=4&cid=124","http://app.suning.com/android/app?gid=4&cid=179"]
    DETAIL_URLS="//div[@class='app-result']/ul/li/dl/dd/div[@class='name']/h3/a"
    DOWNLOAD_URL="//span[@class='dl2pc']/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//dl[@class='detail-top fl']/dd/h3"
    CATEGORY="//p[@class='bread-nav']/a[4]"
    DOWNLOAD_COUNT="//dl[@class='detail-main clearfix']/dd[1]/p[2]/span"
    UPLOAD_TIME="//dl[@class='detail-main clearfix']/dd[2]/p[2]/span"
    RATING="//div[@class='clearfix']/i"

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.text)*20)
        except Exception as e:
            return None
        return rating
