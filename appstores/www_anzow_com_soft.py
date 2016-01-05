# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.anzow.com"
    START_URLS=["http://www.anzow.com/Game.shtml","http://www.anzow.com/Software-typeid-JNKQEMC8.shtml","http://www.anzow.com/Software-typeid-JNKQHMR0.shtml","http://www.anzow.com/Software-typeid-JNKQKNP4.shtml","http://www.anzow.com/Software-typeid-JNKQNOO0.shtml","http://www.anzow.com/Software-typeid-JNKQQPM8.shtml","http://www.anzow.com/Software-typeid-JNKRDQL8.shtml","http://www.anzow.com/Software-typeid-JNLOPMR8.shtml","http://www.anzow.com/Software-typeid-JNLPCOF0.shtml","http://www.anzow.com/Software-typeid-JNLPLRP8.shtml","http://www.anzow.com/Software-typeid-JNLPPMP8.shtml","http://www.anzow.com/Software-typeid-JNLQCOE0.shtml","http://www.anzow.com/Software-typeid-JNLQFPI4.shtml","http://www.anzow.com/Software-typeid-JNLQIQN0.shtml","http://www.anzow.com/Software-typeid-JNLQLRR8.shtml","http://www.anzow.com/Software-typeid-JNLQPNC8.shtml","http://www.anzow.com/Software-typeid-JNLRCOI0.shtml","http://www.anzow.com/Software-typeid-JNLRFPN4.shtml","http://www.anzow.com/Software-typeid-JNLRIRD0.shtml"]
    DETAIL_URLS="//div[@class='box boxsbg']/dl/dd[@class='down_title']/h2/a"
    DOWNLOAD_URL="//div[@class='contentdbtn']/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//dl[@class='down_info clear']/dd/div[1]/h1"
    CATEGORY="//dl[@class='down_info clear']/dd/dl/dt/ul/li[1]/a"
    RATING="//dl[@class='down_info clear']/dd/dl/dt/ul/li[7]/strong"
    UPLOAD_TIME="//dl[@class='down_info clear']/dd/dl/dt/ul/li[9]"

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

    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            star_str = ele.text
            full_star_num = star_str.count("★")
            rating = str(float(full_star_num*20))
        except Exception as e:
            return None
        return rating