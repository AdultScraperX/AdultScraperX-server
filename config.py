import logging
# 格式化
from app.formatter.CaribbeanFormatter import CaribbeanFormatter
from app.formatter.ReMediaMatterFormatter import ReMediaMatterFormatter
from app.formatter.censoredFormatter import CensoredFormatter
from app.formatter.onePondoFormatter import OnePondoFormatter
from app.formatter.tenMusumeFormatter import TenMusumeFormatter
from app.formatter.data18Formatter import Data18Formatter
from app.formatter.basicFormatter import BasicFormater
# 爬虫
from app.spider.arzon import Arzon
from app.spider.javbus import Javbus
from app.spider.onejav import Onejav
from app.spider.caribbean import Caribbean
from app.spider.arzon_anime import ArzonAnime
from app.spider.onePondo import OnePondo
from app.spider.tenMusume import TenMusume
from app.spider.data18 import Data18

HOST = '0.0.0.0'
PORT = 9999
DEBUG = False

SERVE_ADMIN_TOKEN = 'theBestAVScraper'

MONGODB_HOST = 'mineserver.top'
MONGODB_PORT = 50000
MONGODB_DBNAME = 'adultscraperx'
MONGODB_USER = 'adultscraperx'
MONGODB_PWD = 'adultscraperx'

IMG_R = 373
IMG_W = 800
IMG_H = 538


logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s',
                    # filename='AdultScraperX-server.log',
                    # filemode='a',
                    level=logging.INFO)

SOURCE_LIST = {
    # 有码搜刮
    'censored': [
        # 常规有码影片搜刮
        {
            "pattern": "\w+[\ -]?\d{3}",
            'formatter': CensoredFormatter,
            'webList': [Arzon, Javbus, Onejav]
        }],
    # 无码搜刮
    'uncensored': [
        # Caribbean
        {
            "pattern": "\d{6}\ \d{3}",
            'formatter': CaribbeanFormatter,
            'webList': [Caribbean]
        },
        # one_pondo
        {
            "pattern": "\d{6}\ \d{3}",
            'formatter': OnePondoFormatter,
            'webList': [OnePondo]
        },
        # # Pacopacomama
        # {
        #     "pattern": "[a-zA-Z]+[\ -]?\d{3}",
        #     'formatter': PacopacomamaFormatter,
        #     'webList': [Pacopacomama]
        # },
        # _10musume
        {
            "pattern": "\d{6}\ \d{2}",
            'formatter': TenMusumeFormatter,
            'webList': [TenMusume]
        },
        # # Muramura
        # {
        #     "pattern": "[a-zA-Z]+[\ -]?\d{3}",
        #     'formatter': MuramuraFormatter,
        #     'webList': [Muramura]
        # }
    ],

    # 动漫搜刮
    'animation': [
        {
            'pattern': '.+',
            'formatter': ReMediaMatterFormatter,
            'webList': [ArzonAnime]
        }
    ],

    # 欧美搜刮
    'europe': [
        {
            "pattern": ".+",
            'formatter': Data18Formatter,
            'webList': [Data18]
        }
    ]
}
