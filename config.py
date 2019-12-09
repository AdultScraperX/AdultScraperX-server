import logging

# 格式化

# 爬虫

HOST = '0.0.0.0'
PORT = 9999
DEBUG = False

# 服务端版本号
SERVER_VERSION = 1.0

# 是否开启用户认证
USER_CHECK = False

# 设置缓存标志
CacheTag = '--noCache'

# 管理员TOKEN
SERVE_ADMIN_TOKEN = 'theBestAVScraper'

MONGODB_HOST = 'adultscraperx-mongo-db'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'adultscraperx'
MONGODB_USER = 'adultscraperx'
MONGODB_PWD = 'adultscraperx'

# 设置浏览器驱动
BROWSER_DRIVE = 'chrome'

# 图片处理默认值
IMG_R = 373
IMG_W = 800
IMG_H = 538

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s',
                    # filename='AdultScraperX-server.log',
                    # filemode='a',
                    level=logging.INFO)
