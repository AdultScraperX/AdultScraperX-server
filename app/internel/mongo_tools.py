# -*- coding:utf-8 -*-
import config as CONFIG
import pymongo

connection = None
database = None


def getConnection():
    global connection
    if connection is None:
        connection = pymongo.MongoClient(host=CONFIG.MONGODB_HOST, port=CONFIG.MONGODB_PORT)
    return connection


def getDatabase():
    global database
    if database is None:
        database = getConnection()[CONFIG.MONGODB_DBNAME]
        database.authenticate(CONFIG.MONGODB_USER, CONFIG.MONGODB_PWD)
    return database


def getCollection(collection):
    return getDatabase()[collection]

