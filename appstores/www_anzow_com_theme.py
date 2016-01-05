# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.anzow.com"
    START_URLS=["http://www.anzow.com/theme_type.shtml?tid=JNLMPOE8","http://www.anzow.com/theme_type.shtml?tid=JNMQMOJ8","http://www.anzow.com/theme_type.shtml?tid=JNLNCPG0","http://www.anzow.com/theme_type.shtml?tid=JNLNFQH4","http://www.anzow.com/theme_type.shtml?tid=JNLNIRJ0","http://www.anzow.com/theme_type.shtml?tid=JNMOIPH8","http://www.anzow.com/theme_type.shtml?tid=JNMOLQQ8","http://www.anzow.com/theme_type.shtml?tid=JNMOPMG0","http://www.anzow.com/theme_type.shtml?tid=JNMPCNP4","http://www.anzow.com/theme_type.shtml?tid=JNMPFPJ0","http://www.anzow.com/theme_type.shtml?tid=JNMPIRC8","http://www.anzow.com/theme_type.shtml?tid=JNMPPOD0","http://www.anzow.com/theme_type.shtml?tid=JNMQCPN4","http://www.anzow.com/theme_type.shtml?tid=JNMQFRI0","http://www.anzow.com/theme_type.shtml?tid=JNNOKNH8","http://www.anzow.com/theme_type.shtml?tid=JNMQJMO8"]
    DETAIL_URLS="//div[@class='pics-tab w-678 pdl7']/ul/li/p/a"
    DOWNLOAD_URL="//a[@id='downPicSrc']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@id='picinfo']"
    CATEGORY="//div[@class='position']/a[3]"
    DOWNLOAD_COUNT="//span[@id='zt_download_count']"
    UPLOAD_TIME="//div[@id='Article']/h1/span[1]"

    def get_upload_time(self,detail_page_driver):
        if self.UPLOAD_TIME is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.UPLOAD_TIME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            upload_time = util.unify_data(ele.text.split(" ")[0])
        except Exception as e:
            return None
        return upload_time

    def get_appname(self,detail_page_driver):
        if self.APPNAME is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.APPNAME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            appName = ele.text.split("(")[0]
        except Exception as e:
            return None
        return appName
