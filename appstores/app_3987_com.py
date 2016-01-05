# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="app.3987.com"
    START_URLS=["http://app.3987.com/list-11-3362-0-1.html","http://app.3987.com/list-11-3363-0-1.html","http://app.3987.com/list-11-3364-0-1.html","http://app.3987.com/list-11-3367-0-1.html","http://app.3987.com/list-11-3368-0-1.html","http://app.3987.com/list-11-3369-0-1.html","http://app.3987.com/list-11-3371-0-1.html","http://app.3987.com/list-11-3372-0-1.html","http://app.3987.com/list-11-3373-0-1.html","http://app.3987.com/list-11-3374-0-1.html","http://app.3987.com/list-11-3375-0-1.html","http://app.3987.com/list-11-3376-0-1.html","http://app.3987.com/list-11-3433-0-1.html","http://app.3987.com/list-11-3366-0-1.html","http://app.3987.com/list-11-3437-0-1.html","http://app.3987.com/list-12-3377-0-1.html","http://app.3987.com/list-12-3378-0-1.html","http://app.3987.com/list-12-3379-0-1.html","http://app.3987.com/list-12-3381-0-1.html","http://app.3987.com/list-12-3382-0-1.html","http://app.3987.com/list-12-3385-0-1.html","http://app.3987.com/list-12-3387-0-1.html","http://app.3987.com/list-12-3389-0-1.html","http://app.3987.com/list-12-3390-0-1.html","http://app.3987.com/list-12-3391-0-1.html","http://app.3987.com/list-12-3393-0-1.html","http://app.3987.com/list-12-3394-0-1.html","http://app.3987.com/list-12-3395-0-1.html","http://app.3987.com/list-12-3396-0-1.html","http://app.3987.com/list-12-3398-0-1.html","http://app.3987.com/list-12-3399-0-1.html","http://app.3987.com/list-12-3434-0-1.html","http://app.3987.com/list-12-3400-0-1.html","http://app.3987.com/list-12-3401-0-1.html","http://app.3987.com/list-12-3392-0-1.html"]
    DETAIL_URLS="//ul[@class='app_list_box clearfix']/li/div[@class='list_in']/div[@class='list_right']/p[@class='r_name']/a"
    DOWNLOAD_URL="//div[@class='wpxz']/div[@class='wpxz1']/div[@class='udown_box fl']/div[@class='xz_top']/div[@class='ulw']/a[1]"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//h1[@class='info_title']"
    CATEGORY="//div[@class='detail_right']/div[@class='detail_con clearfix']/p[1]/a"
    UPLOAD_TIME="//div[@class='detail_right']/div[@class='detail_con clearfix']/p[2]"
    RATING="//div[@class='detail_right']/div[@class='detail_con clearfix']/p[7]/i"
    DOWNLOAD_COUNT="//div[@class='detail_con clearfix']/p[3]/span[@id='hits']"


    def get_rating(self,detail_page_driver):
        if self.RATING is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("class").split("star")[2])*20)
        except Exception as e:
            return None
        return rating
