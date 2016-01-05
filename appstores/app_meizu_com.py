# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="app.meizu.com"
    START_URLS=["http://app.meizu.com/apps/public/category/103/free/feed/index/0/18","http://app.meizu.com/apps/public/category/100/free/feed/index/0/18","http://app.meizu.com/apps/public/category/102/free/feed/index/0/18","http://app.meizu.com/apps/public/category/106/free/feed/index/0/18","http://app.meizu.com/apps/public/category/104/free/feed/index/0/18","http://app.meizu.com/apps/public/category/9014/free/feed/index/0/18","http://app.meizu.com/apps/public/category/101/free/feed/index/0/18","http://app.meizu.com/apps/public/category/338/free/feed/index/0/18","http://app.meizu.com/apps/public/category/339/free/feed/index/0/18","http://app.meizu.com/apps/public/category/344/free/feed/index/0/18","http://app.meizu.com/apps/public/category/105/free/feed/index/0/18","http://app.meizu.com/games/public/category/1006/free/feed/index/0/18","http://app.meizu.com/games/public/category/1000/free/feed/index/0/18","http://app.meizu.com/games/public/category/1005/free/feed/index/0/18","http://app.meizu.com/games/public/category/1001/free/feed/index/0/18","http://app.meizu.com/games/public/category/1004/free/feed/index/0/18","http://app.meizu.com/games/public/category/9012/free/feed/index/0/18","http://app.meizu.com/games/public/category/1003/free/feed/index/0/18","http://app.meizu.com/games/public/category/1007/free/feed/index/0/18","http://app.meizu.com/games/public/category/9013/free/feed/index/0/18","http://app.meizu.com/games/public/category/1002/free/feed/index/0/18"]
    DETAIL_URLS="//div[@class='app download_container']/div/div/a[1]"
    DOWNLOAD_URL="//div[@class='app_download download_container']/div"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='detail_top']/h3"
    RATING="//div[@class='app_download download_container']/ul/li[1]/div/div"
    CATEGORY="//div[@class='app_download download_container']/ul/li[2]/div/a"
    DOWNLOAD_COUNT="//div[@class='app_download download_container']/ul/li[5]/div/span"
    UPLOAD_TIME="//div[@class='app_download download_container']/ul/li[7]/div/span"

    def get_rating(self,detail_page_driver):
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("data-num"))*20)
        except Exception as e:
            return None
        return rating

    def get_download_url(self,detail_page_driver):
        download_url = None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_URL)
        except selenium_exception.NoSuchElementException as e:
            try:
                detail_page_driver.refresh()
            except selenium_exception.TimeoutException as e:
                pass
            try:
                ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_URL)
            except selenium_exception.NoSuchElementException as e:
                return download_url
        try:
            appid=ele.get_attribute('data-appid')
            tmp_url="http://app.meizu.com/apps/public/download.json?app_id="+appid
            import requests
            import config
            r=requests.get(tmp_url,timeout=config.REQUESTS_TIMEOUT)
            if r.status_code==200:
                import json
                return json.loads(r.content)['value']['downloadUrl']
            else:
                return download_url
        except Exception as e:
                return download_url