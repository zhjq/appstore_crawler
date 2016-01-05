# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.lenovomm.com"
    START_URLS=["http://www.lenovomm.com/category/class/2023_1038_0_flat_1.html","http://www.lenovomm.com/category/class/2023_1028_0_flat_1.html","http://www.lenovomm.com/category/class/2023_1048_0_flat_1.html","http://www.lenovomm.com/category/class/2023_1052_0_flat_1.html","http://www.lenovomm.com/category/class/2023_1034_0_flat_1.html","http://www.lenovomm.com/category/class/2023_1030_0_flat_1.html","http://www.lenovomm.com/category/class/2023_1040_0_flat_1.html","http://www.lenovomm.com/category/class/2023_1042_0_flat_1.html","http://www.lenovomm.com/category/class/2023_1060_0_flat_1.html","http://www.lenovomm.com/category/class/2023_1036_0_flat_1.html","http://www.lenovomm.com/category/class/2023_1046_0_flat_1.html","http://www.lenovomm.com/category/class/2023_1058_0_flat_1.html","http://www.lenovomm.com/category/class/2023_1050_0_flat_1.html","http://www.lenovomm.com/category/class/2023_1032_0_flat_1.html","http://www.lenovomm.com/category/class/2023_1062_0_flat_1.html","http://www.lenovomm.com/category/class/2023_1054_0_flat_1.html","http://www.lenovomm.com/category/class/2023_1066_0_flat_1.html","http://www.lenovomm.com/category/class/2023_1026_0_flat_1.html","http://www.lenovomm.com/category/class/2023_1056_0_flat_1.html","http://www.lenovomm.com/category/class/2023_1068_0_flat_1.html","http://www.lenovomm.com/category/class/2021_1002_0_flat_1.html","http://www.lenovomm.com/category/class/2021_1006_0_flat_1.html","http://www.lenovomm.com/category/class/2021_1004_0_flat_1.html","http://www.lenovomm.com/category/class/2021_1018_0_flat_1.html","http://www.lenovomm.com/category/class/2021_1008_0_flat_1.html","http://www.lenovomm.com/category/class/2021_2025_0_flat_1.html","http://www.lenovomm.com/category/class/2021_1022_0_flat_1.html","http://www.lenovomm.com/category/class/2021_1010_0_flat_1.html","http://www.lenovomm.com/category/class/2021_1012_0_flat_1.html","http://www.lenovomm.com/category/class/2021_1014_0_flat_1.html"]
    DETAIL_URLS="//ul[@class='apps']/li/div/a[@class='fblue f13 fb appName txtCut orange ftransition']"
    DOWNLOAD_URL="//li[@class='liLast']/a[@id='downAPK']"
    NEXTPAGE="//a[text()='下一页 >']"
    APPNAME="//div[@class='ff-wryh detailAppname txtCut']/h1"
    CATEGORY="//div[@class='crumbNavBox repeatXbg']/div/a[3]"
    DOWNLOAD_COUNT="//div[@class='f12 detailDownNum cb clearfix']/span"
    UPLOAD_TIME="//ul[@class='detailAppInfo fl']/li[5]/span"
    RATING="//div[@class='f12 detailDownNum cb clearfix']/p"

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("score"))*20)
        except Exception as e:
            return None
        return rating
