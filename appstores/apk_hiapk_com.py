# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="apk.hiapk.com"
    START_URLS=["http://apk.hiapk.com/apps/MediaAndVideo","http://apk.hiapk.com/apps/DailyLife","http://apk.hiapk.com/apps/Social","http://apk.hiapk.com/apps/Finance","http://apk.hiapk.com/apps/Tools","http://apk.hiapk.com/apps/TravelAndLocal","http://apk.hiapk.com/apps/Communication","http://apk.hiapk.com/apps/Shopping","http://apk.hiapk.com/apps/Reading","http://apk.hiapk.com/apps/Education","http://apk.hiapk.com/apps/NewsAndMagazines","http://apk.hiapk.com/apps/HealthAndFitness","http://apk.hiapk.com/apps/AntiVirus","http://apk.hiapk.com/apps/Browser","http://apk.hiapk.com/apps/Productivity","http://apk.hiapk.com/apps/Personalization","http://apk.hiapk.com/apps/Input","http://apk.hiapk.com/apps/Photography","http://apk.hiapk.com/games/OnlineGames","http://apk.hiapk.com/games/Casual","http://apk.hiapk.com/games/RolePlaying","http://apk.hiapk.com/games/BrainAndPuzzle","http://apk.hiapk.com/games/Shooting","http://apk.hiapk.com/games/Sports","http://apk.hiapk.com/games/Children","http://apk.hiapk.com/games/Chess","http://apk.hiapk.com/games/Strategy","http://apk.hiapk.com/games/Simulation","http://apk.hiapk.com/games/Racing"]
    DETAIL_URLS="//span[@class='list_title font14_2']/a"
    DOWNLOAD_URL="//a[@id='appInfoDownUrl']"
    NEXTPAGE="//span[@class='page_item page_next page_able']/.."
    APPNAME="//div[@id='appSoftName']"
    UPLOAD_TIME="//div[@class='detail_right']"
    DOWNLOAD_COUNT="//div[@class='detail_right']"
    RATING="//div[@id='appIconTips']/div"
    CATEGORY="//a[@id='categoryLink']"


    def get_upload_time(self,detail_page_driver):
        try:
            ele = detail_page_driver.find_element_by_xpath(self.UPLOAD_TIME)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            upload_time = util.unify_data(ele.text.split("上架时间： ")[1].split('相关推荐')[0].strip())
        except Exception as e:
            return None
        return upload_time

    def get_download_count(self,detail_page_driver):
        try:
            ele = detail_page_driver.find_element_by_xpath(self.DOWNLOAD_COUNT)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            if ele.text.split("热度： ")[1].split('大小：')[0].strip() == "小于1千热度":
                return "500"
            download_count = util.unify_download_count(ele.text.split("热度： ")[1].split('大小：')[0].strip())
        except Exception as e:
            return None
        return download_count

    def get_rating(self,detail_page_driver):
        try:
            ele = detail_page_driver.find_element_by_xpath(self.RATING)
        except selenium_exception.NoSuchElementException as e:
            return None
        try:
            rating = str(float(ele.get_attribute("class").split(" ")[2].split("_")[2])*2)
        except Exception as e:
            return None
        return rating
