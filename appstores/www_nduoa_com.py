# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.nduoa.com"
    START_URLS=["http://www.nduoa.com/cat978","http://www.nduoa.com/cat980","http://www.nduoa.com/cat193","http://www.nduoa.com/cat979","http://www.nduoa.com/cat84","http://www.nduoa.com/cat85","http://www.nduoa.com/cat87","http://www.nduoa.com/cat88","http://www.nduoa.com/cat89","http://www.nduoa.com/cat974","http://www.nduoa.com/cat975","http://www.nduoa.com/cat976","http://www.nduoa.com/cat97","http://www.nduoa.com/cat98","http://www.nduoa.com/cat99","http://www.nduoa.com/cat101","http://www.nduoa.com/cat100","http://www.nduoa.com/cat96","http://www.nduoa.com/cat95","http://www.nduoa.com/cat94","http://www.nduoa.com/cat92","http://www.nduoa.com/cat93"]
    DETAIL_URLS="//div[@class='item']/ul[@class='apklist clearfix']/li/div[@class='name']/a"
    DOWNLOAD_URL="//div[@class='downloadWrap']/div[@class='normal']/a[@id='BDTJDownload']"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='head']/div[@class='name']/span[@class='title']"
    CATEGORY="//div[@id='breadcrumbs']/span[3]"
    DOWNLOAD_COUNT="//div[@class='levelCount']/span[@class='count']"

    def get_rating(self,detail_page_driver):
        try:
            full_star_num = len(detail_page_driver.find_elements_by_xpath("//div[@class='starWrap']/span/s[@class='full']"))
            half_star_num = len(detail_page_driver.find_elements_by_xpath("//div[@class='starWrap']/span/s[@class='half']"))
            rating = str(20*full_star_num + 10*half_star_num)
        except Exception as e:
            return None
        return rating
