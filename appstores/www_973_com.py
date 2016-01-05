# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception
import requests

class Store(Base):
    SOURCE="www.973.com"
    START_URLS=["http://www.973.com/dongzuomaoxian","http://www.973.com/xiuxianyizhi","http://www.973.com/jingyingcelue","http://www.973.com/tiyujingsu","http://www.973.com/qipaitiandi","http://www.973.com/feixingsheji","http://www.973.com/jiaosebanyan","http://www.973.com/yinyueshejiao","http://www.973.com/monifuzhu","http://www.973.com/xuanhuanxiuxian","http://www.973.com/rimantongren","http://www.973.com/jingjigedou"] 
    DETAIL_URLS="//div[@id='fl']/p/u/a"
    DOWNLOAD_URL="//div[@id='n']/p[2]/i/a[1]"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@id='ne']/h1"
    CATEGORY="//p[@id='p']/a[2]"
    UPLOAD_TIME="//p[@id='nj']/i[4]"
    DOWNLOAD_COUNT="//p[@id='nj']/i[6]"
    RATING="//p[@id='nj']/s[1]"

    def get_download_count(self,detail_page_driver):
        if self.DOWNLOAD_COUNT is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_COUNT)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            download_count = util.unify_download_count(ele.text.split(" ")[0])
        except Exception as e:
            return None
        return download_count

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("id").split("s")[1])*10)
        except Exception as e:
            return None
        return rating
    
    def get_download_url(self,detail_page_driver):
        download_url = None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_URL)
        except selenium_exception.NoSuchElementException as e:
            detail_page_driver.refresh()
            try:
                ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_URL)
            except selenium_exception.NoSuchElementException as e:
                return download_url
        try:
            download_url_param = ele.get_attribute("onclick").split("(")[1].split(")")[0]
            gid = download_url_param.split(",")[0]
            art = download_url_param.split("\'")[1].split("\'")[0]
            download_url_temp = 'http://www.973.com'+'/s.php?gid=' + gid + '&art=' + art + '&ac=web'
            import config
            resp =  requests.get(download_url_temp, timeout = config.REQUESTS_TIMEOUT)
            download_url = resp.content
        except:
            return None
        return download_url
