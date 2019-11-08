import config as CONFIG
import pymongo


def getConnection():
    client = pymongo.MongoClient(host=CONFIG.MONGODB_HOST, port=CONFIG.MONGODB_PORT)
