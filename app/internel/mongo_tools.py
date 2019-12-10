# -*- coding:utf-8 -*-
import pymongo

connection = None
database = None


def getConnection():
    global connection
    if connection is None:
        connection = pymongo.MongoClient(host=config.MONGODB_HOST, port=config.MONGODB_PORT)
    return connection


def getDatabase():
    global database
    if database is None:
        database = getConnection()[config.MONGODB_DBNAME]
        database.authenticate(config.MONGODB_USER, config.MONGODB_PWD)
    return database


def getCollection(collection):
    return getDatabase()[collection]

