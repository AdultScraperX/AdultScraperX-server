import logging
# 格式化
from app.formatter.HeydougaFormatter import HeydougaFormatter
from app.formatter.HeydougaOfficialFormatter import HeydougaOfficialFormatter
from app.formatter.CaribbeancomprFormatter import CaribbeancomprFormatter
from app.formatter.CaribbeanFormatter import CaribbeanFormatter
from app.formatter.HeyzoFormatter import HeyzoFormatter
from app.formatter.ReMediaMatterFormatter import ReMediaMatterFormatter
from app.formatter.TokyoHotFormatter import TokyoHotFormatter
from app.formatter.censoredFormatter import CensoredFormatter
from app.formatter.fc2ppvFormatter import Fc2ppvFormater
from app.formatter.onePondoFormatter import OnePondoFormatter
from app.formatter.tenMusumeFormatter import TenMusumeFormatter
from app.formatter.data18Formatter import Data18Formatter
from app.formatter.basicFormatter import BasicFormater

# 爬虫
from app.spider.arzon import Arzon
from app.spider.caribbeancompr import Caribbeancompr
from app.spider.javbus import Javbus
from app.spider.javr import Javr
from app.spider.onejav import Onejav
from app.spider.caribbean import Caribbean
from app.spider.arzon_anime import ArzonAnime
from app.spider.onePondo import OnePondo
from app.spider.pacoPacoMama import PacoPacoMama
from app.spider.tenMusume import TenMusume
from app.spider.data18 import Data18
from app.spider.heydougaOfficial import HeydougaOfficial

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
        # FC2PPV
        {
            "pattern": "(fc|Fc|FC).*\d{6,7}",
            'formatter': Fc2ppvFormater,
            'webList': [Javr]
        },

        # Heydouga for official  4037/427   3004/q1234   ppv-051619_095   hzo-1992
        {
            "pattern": r"[0-9]{4}\D[0-9]{1,5}|[0-9]{4}\D(Q|q)[0-9]{1,5}|[0-9]{4}\D(.{3})\D[0-9]{4}|[0-9]{4}\D(.{3})\D[0-9]{6}\D[0-9]{3}",
            'formatter': HeydougaOfficialFormatter,
            'webList': [HeydougaOfficial]
        },
        # Heydouga for javr
        {
            "pattern": "(Heydouga|HEYDOUGA|heydouga).*\d+.*\d+[.*\d]{0,1}",
            'formatter': HeydougaFormatter,
            'webList': [Javr]
        },
        # Heyzo
        {
            "pattern": "(Heyzo|HEYZO|heyzo).*\d{4}",
            'formatter': HeyzoFormatter,
            'webList': [Javr]
        },
        # TokyoHot
        {
            "pattern": "(tokyo|TOKYO|Tokyo).*[A-Za-z]+[\ -]?\d+",
            'formatter': TokyoHotFormatter,
            'webList': [Javr]
        },
        # Caribbean
        {
            "pattern": "\d{6}.\d{3}",
            'formatter': CaribbeanFormatter,
            'webList': [Caribbean, Javr]
        },
        # Caribbeancompr
        {
            "pattern": "\d{6}.\d{3}",
            'formatter': CaribbeancomprFormatter,
            'webList': [Caribbeancompr, Javr]
        },
        # Pacopacomama
        {
            "pattern": "\d{6}.\d{3}",
            'formatter': OnePondoFormatter,
            'webList': [PacoPacoMama, Javr]
        },
        # _10musume
        {
            "pattern": "\d{6}.\d{2}",
            'formatter': TenMusumeFormatter,
            'webList': [TenMusume, Javr]
        },
        # one_pondo
        {
            "pattern": "\d{6}.\d{3}",
            'formatter': OnePondoFormatter,
            'webList': [OnePondo, Javr]
        },
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
