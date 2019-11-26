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
from app.formatter.HeyzoOfficialFormatter import HeyzoOfficialFormatter
from app.formatter.msgBloggFormatter import MGSBloggFormatter

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
from app.spider.HeyzoOfficial import HeyzoOfficial
from app.spider.mgsBlogg import MGSBlogg

HOST = '0.0.0.0'
PORT = 9999
DEBUG = False

#设置缓存标志
CacheTag='---'

#管理员TOKEN
SERVE_ADMIN_TOKEN = 'theBestAVScraper'

MONGODB_HOST = 'mineserver.top'
MONGODB_PORT = 50000
MONGODB_DBNAME = 'adultscraperx'
MONGODB_USER = 'adultscraperx'
MONGODB_PWD = 'adultscraperx'

#图片处理默认值
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
            #"pattern": r"\w+[\ -]?\d{1,3}",
            "pattern": r"\w+[a-z]{2,5}\D{1}\d{1,3}|[a-z]{2,5}\d{1,3}",
            'formatter': CensoredFormatter,
            'webList': [Arzon, Javbus, Onejav]
        },
        #  MGSBlogg 
        {
            "pattern": r"200GANA\D{1}[0-9]{4}|200GANA[0-9]{4}|259LUXU\D{1}[0-9]{4}|259LUXU[0-9]{4}|SIRO\D{1}[0-9]{4}|SIRO[0-9]{4}|300MIUM\D{1}[0-9]{3}|300MIUM[0-9]{3}|300MAAN\D{1}[0-9]{3}|300MAAN[0-9]{3}|261ARA\D{1}[0-9]{3}|261ARA[0-9]{3}|277DCV\D{1}[0-9]{3}|277DCV[0-9]{3}|230ORE\D{1}[0-9]{3}|230ORE[0-9]{3}|300NTK\D{1}[0-9]{3}|300NTK[0-9]{3}|336KNB\D{1}[0-9]{3}|336KNB[0-9]{3}|320MMGH\D{1}[0-9]{3}|320MMGH[0-9]{3}|332NAMA\D{1}[0-9]{3}|332NAMA[0-9]{3}|279UTSU\D{1}[0-9]{3}|279UTSU[0-9]{3}|345SIMM\D{1}[0-9]{3}|345SIMM[0-9]{3}|276KITAIKE\D{1}[0-9]{3}|276KITAIKE[0-9]{3}|326SCP\D{1}[0-9]{3}|326SCP[0-9]{3}|326SPOR\D{1}[0-9]{3}|326SPOR[0-9]{3}|348NTR\D{1}[0-9]{3}|348NTR[0-9]{3}|326URF\D{1}[0-9]{3}|326URF[0-9]{3}|274ETQT\D{1}[0-9]{3}|274ETQT[0-9]{3}|326EVA\D{1}[0-9]{3}|326EVA[0-9]{3}|409BZDC\D{1}[0-9]{3}|409BZDC[0-9]{3}",
            'formatter': MGSBloggFormatter,
            'webList': [MGSBlogg]
        }
    ],
    # 无码搜刮
    'uncensored': [

        # Heydouga for official  4037/427   3004/q1234   ppv-051619_095   hzo-1992
        {
            "pattern": r"Heydouga\D{1}[0-9]{4}\D[0-9]{1,5}|Heydouga[0-9]{4}\D[0-9]{1,5}|Heydouga\D{1}[0-9]{4}\D(Q|q)[0-9]{1,5}|Heydouga[0-9]{4}\D(Q|q)[0-9]{1,5}|Heydouga\D{1}[0-9]{4}\D(.{3})\D{1}[0-9]{4}|Heydouga[0-9]{4}\D(.{3})\D{1}[0-9]{4}|Heydouga\D{1}[0-9]{4}\D(.{3})\D[0-9]{6}\D{1}[0-9]{3}|Heydouga[0-9]{4}\D(.{3})\D[0-9]{6}\D{1}[0-9]{3}",
            'formatter': HeydougaOfficialFormatter,
            'webList': [HeydougaOfficial]
        },
        # Heydouga for javr
        {
            "pattern": r"[Heydouga|HEYDOUGA|heydouga].*\d+.*\d+[.*\d]{0,1}",
            'formatter': HeydougaFormatter,
            'webList': [Javr]
        },
        # heyzo for official  1234
        {
            "pattern": r"hzo\D{1}[0-9]{4}|heyzo\D{1}[0-9]{4}|hzo[0-9]{4}|heyzo[0-9]{4}",
            'formatter': HeyzoOfficialFormatter,
            'webList': [HeyzoOfficial]
        },

        # Heyzo for javr
        {
            "pattern": r"[Heyzo|HEYZO|heyzo].*\d{4}",
            'formatter': HeyzoFormatter,
            'webList': [Javr]
        },
        # TokyoHot for javr
        {
            "pattern": r"[tokyo|TOKYO].*[A-Za-z]+[\ -]?\d+",
            'formatter': TokyoHotFormatter,
            'webList': [Javr]
        },
        # FC2PPV for javr
        {
            "pattern": r"[fc|Fc|FC].*\d{6}",
            'formatter': Fc2ppvFormater,
            'webList': [Javr]
        },
        # Caribbean
        {
            # "pattern": r"Carib\D{1}\d{6}.\d{3}|Caribbean\D{1}\d{6}.\d{3}|Carib\d{6}.\d{3}|Caribbean\d{6}.\d{3}|\d{6}.\d{3}",
            "pattern": r"\d{6}.\d{3}",
            'formatter': CaribbeanFormatter,
            'webList': [Caribbean, Javr]
        },
        # Caribbeancompr
        {
            # "pattern": r"Carib\D{1}\d{6}.\d{3}|Caribbean\D{1}\d{6}.\d{3}|Carib\d{6}.\d{3}|Caribbean\d{6}.\d{3}|\d{6}.\d{3}",
            "pattern": r"\d{6}.\d{3}",
            'formatter': CaribbeancomprFormatter,
            'webList': [Caribbeancompr, Javr]
        },
        # Pacopacomama
        {
            # "pattern": r"Pacopacomama\D{1}\d{6}.\d{3}|Pacopa\D{1}\d{6}.\d{3}|pacopaco\D{1}\d{6}.\d{3}|pacomama\D{1}\d{6}.\d{3}|Pacopacomama\d{6}.\d{3}|Pacopa\d{6}.\d{3}|pacopaco\d{6}.\d{3}|pacomama\d{6}.\d{3}|\d{6}.\d{3}",
            "pattern": r"\d{6}.\d{3}",
            'formatter': OnePondoFormatter,
            'webList': [PacoPacoMama, Javr]
        },
        # 10musume
        {
            # "pattern": r"10musume\D{1}|10mus\D{1}\d{6}.\d{2}|10mu\D{1}\d{6}.\d{2}|10musume\d{6}.\d{2}|10mus\d{6}.\d{2}|10mu\d{6}.\d{2}|\d{6}.\d{2}",
            "pattern": r"\d{6}.\d{3}",
            'formatter': TenMusumeFormatter,
            'webList': [TenMusume, Javr]
        },
        # one_pondo
        {
            # "pattern": r"onepondo\D{1}\d{6}.\d{3}|Pondo\D{1}\d{6}.\d{3}|TokyoPondo\D{1}\d{6}.\d{3}|1ppondo\D{1}\d{6}.\d{3}|onepondo\d{6}.\d{3}|Pondo\d{6}.\d{3}|TokyoPondo\d{6}.\d{3}|1ppondo\d{6}.\d{3}|\d{6}.\d{3}",
            "pattern": r"\d{6}.\d{3}",
            'formatter': OnePondoFormatter,
            'webList': [OnePondo, Javr]
        }

    ],

    # 动漫搜刮
    'animation': [
        {
            'pattern': r'[a-z]{1,5}\D{1}[0-9]{1,5}|[a-z]{1,5}[0-9]{1,5}|.+',
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
