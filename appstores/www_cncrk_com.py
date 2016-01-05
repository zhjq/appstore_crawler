# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.cncrk.com"
    START_URLS=["http://www.cncrk.com/shouji/s_238_1.html","http://www.cncrk.com/shouji/s_237_1.html","http://www.cncrk.com/shouji/s_235_1.html","http://www.cncrk.com/shouji/s_234_1.html","http://www.cncrk.com/shouji/s_232_1.html","http://www.cncrk.com/shouji/s_231_1.html","http://www.cncrk.com/shouji/s_229_1.html","http://www.cncrk.com/shouji/s_228_1.html","http://www.cncrk.com/shouji/s_268_1.html","http://www.cncrk.com/shouji/s_269_1.html","http://www.cncrk.com/shouji/s_210_1.html","http://www.cncrk.com/shouji/s_211_1.html","http://www.cncrk.com/shouji/s_212_1.html","http://www.cncrk.com/shouji/s_213_1.html","http://www.cncrk.com/shouji/s_214_1.html","http://www.cncrk.com/shouji/s_215_1.html","http://www.cncrk.com/shouji/s_216_1.html","http://www.cncrk.com/shouji/s_217_1.html","http://www.cncrk.com/shouji/s_218_1.html","http://www.cncrk.com/shouji/s_219_1.html","http://www.cncrk.com/shouji/s_220_1.html","http://www.cncrk.com/shouji/s_221_1.html","http://www.cncrk.com/shouji/s_222_1.html","http://www.cncrk.com/shouji/s_223_1.html","http://www.cncrk.com/shouji/s_224_1.html","http://www.cncrk.com/shouji/s_225_1.html","http://www.cncrk.com/shouji/s_226_1.html","http://www.cncrk.com/shouji/s_270_1.html","http://www.cncrk.com/shouji/s_271_1.html","http://www.cncrk.com/shouji/s_272_1.html","http://www.cncrk.com/shouji/s_273_1.html"]
    DETAIL_URLS="//div[@id='softs']/ul/li/span/a"
    DOWNLOAD_URL="//dt[@class='wt']/a[@class='dPage']"
    NEXTPAGE="//i[text()='下一页']/.."
    APPNAME="//div[@id='softtitle']"
    UPLOAD_TIME="//div[@id='softinfo']/ul/li[7]"
    RATING="//div[@id='softinfo']/ul/li[5]/img"
    CATEGORY="//div[@id='currentnav']/a[3]"

    def get_rating(self,detail_page_driver):
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("src").split('images/')[1].split('star')[0])*20)
        except Exception as e:
            return None
        return rating