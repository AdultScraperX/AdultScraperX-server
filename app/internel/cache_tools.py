import threading

import app.internel.mongo_tools as mongoTools


def checkCache(code, type):
    lock = threading.Lock()
    metaInfo = None
    lock.acquire()
    try:
        searchQuery = {
            'code': code,
            'type': type
        }
        collection = mongoTools.getCollection('meta_cache')
        metaInfo = collection.find_one(searchQuery)
        if metaInfo is not None :
            metaInfo = metaInfo['metaData']
    finally:
        lock.release()
        return metaInfo


def setCache(code, metaData, type):
    lock = threading.Lock()
    lock.acquire()
    cacheData = {}
    try:
        cacheData.update({'code': code})
        cacheData.update({'type': type})
        cacheData.update({'metaData': metaData})
        searchQuery = {
            'code': code,
            'type': type
        }
        collection = mongoTools.getCollection('meta_cache')
        metaInfo = collection.find_one(searchQuery)
        if metaInfo is None:
            collection.insert(cacheData)
    finally:
        lock.release()
