# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.play.cn"
    START_URLS=["http://www.play.cn/game/searchgame?type_code=11&class_code=1007&order_type=0#gamelist","http://www.play.cn/game/searchgame?type_code=11&class_code=1003&order_type=0#gamelist","http://www.play.cn/game/searchgame?type_code=11&class_code=1005&order_type=0#gamelist","http://www.play.cn/game/searchgame?type_code=11&class_code=1002&order_type=0#gamelist","http://www.play.cn/game/searchgame?type_code=11&class_code=1014&order_type=0#gamelist","http://www.play.cn/game/searchgame?type_code=11&class_code=1004&order_type=0#gamelist","http://www.play.cn/game/searchgame?type_code=11&class_code=1009&order_type=0#gamelist","http://www.play.cn/game/searchgame?type_code=11&class_code=1013&order_type=0#gamelist","http://www.play.cn/game/searchgame?type_code=11&class_code=1006&order_type=0#gamelist","http://www.play.cn/game/searchgame?type_code=12&class_code=-1&order_type=0#gamelist"]
    DETAIL_URLS="//ul[@id='gameList']/li/a[@class='name']"
    DOWNLOAD_URL="//div[@class='side_b r']/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//div[@class='info_side']/div[@class='fix']/h1"
    CATEGORY="//div[@class='game_layer f_s fix']/div[1]/div[1]/p"
    UPLOAD_TIME="//div[@class='game_layer f_s fix']/div[3]/div[1]/p"
    DOWNLOAD_COUNT="//div[@class='game_layer f_s fix']/div[2]/div[2]/p"

    def get_category(self,detail_page_driver):
        if self.CATEGORY is None:
            return None
        try:
            ele = detail_page_driver.find_element_by_xpath(self.CATEGORY)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            category = ele.text.split("：")[1]
        except Exception as e:
            return None
        return category