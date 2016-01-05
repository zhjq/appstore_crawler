# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import util
from base import Base,selenium_exception

class Store(Base):
    SOURCE="www.eoemarket.com"
    START_URLS=["http://www.eoemarket.com/soft/4_hot_unofficial_hasad_1_1.html","http://www.eoemarket.com/soft/5_hot_unofficial_hasad_1_1.html","http://www.eoemarket.com/soft/8_hot_unofficial_hasad_1_1.html","http://www.eoemarket.com/soft/9_hot_unofficial_hasad_1_1.html","http://www.eoemarket.com/soft/10_hot_unofficial_hasad_1_1.html","http://www.eoemarket.com/soft/15_hot_unofficial_hasad_1_1.html","http://www.eoemarket.com/soft/72_hot_unofficial_hasad_1_1.html","http://www.eoemarket.com/soft/36_hot_unofficial_hasad_1_1.html","http://www.eoemarket.com/soft/37_hot_unofficial_hasad_1_1.html","http://www.eoemarket.com/soft/73_hot_unofficial_hasad_1_1.html","http://www.eoemarket.com/soft/74_hot_unofficial_hasad_1_1.html","http://www.eoemarket.com/soft/75_hot_unofficial_hasad_1_1.html","http://www.eoemarket.com/soft/77_hot_unofficial_hasad_1_1.html","http://www.eoemarket.com/soft/78_hot_unofficial_hasad_1_1.html","http://www.eoemarket.com/soft/79_hot_unofficial_hasad_1_1.html","http://www.eoemarket.com/soft/80_hot_unofficial_hasad_1_1.html","http://www.eoemarket.com/soft/81_hot_unofficial_hasad_1_1.html","http://www.eoemarket.com/game/19_hot_unofficial_hasad_2_1.html","http://www.eoemarket.com/game/20_hot_unofficial_hasad_2_1.html","http://www.eoemarket.com/game/21_hot_unofficial_hasad_2_1.html","http://www.eoemarket.com/game/22_hot_unofficial_hasad_2_1.html","http://www.eoemarket.com/game/31_hot_unofficial_hasad_2_1.html","http://www.eoemarket.com/game/32_hot_unofficial_hasad_2_1.html","http://www.eoemarket.com/game/33_hot_unofficial_hasad_2_1.html","http://www.eoemarket.com/game/35_hot_unofficial_hasad_2_1.html"]
    DETAIL_URLS="//div[@class='app_classf_list clearfix']/div[@class='app_classf_listc']/div[@class='classf_list_item fl ']/div/span/a"
    DOWNLOAD_URL="//div[@class='qrcode_introduce']/span[@class='download_intr']/a"
    NEXTPAGE="//a[text()='下一页']"
    APPNAME="//span[@class='name_appintr']"
    CATEGORY="//div[@class='content_c ']/div[@class='page_info']/ol/li[5]/a"
    UPLOAD_TIME="//span[@class='info_appintr clearfix']/span[2]/em[3]"
    DOWNLOAD_COUNT="//span[@class='info_appintr clearfix']/span[1]/em[3]"
