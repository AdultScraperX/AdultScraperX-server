import logging
import socket
import uuid

import app.internel.mongo_tools as mongoTools


def checkUser(token, userIp, FQDN, port):
    """
    测试用户有效性
    :param token: 插件通信token
    :param userIp: 服务端获取的访问ip
    :param FQDN:  插件上报的前端FQDN
    :param port:  插件上报的前端 plex 端口
    :return: 用户有效True 无效 False
    """
    collection = mongoTools.getCollection('user')
    searchQuery = {'token': token}
    userInfo = collection.find_one(searchQuery)
    if userInfo is not None:
        logging.info(u'用户访问IP：%s' % userIp)
        if userInfo['FQDN'] == '':
            userInfo['FQDN'] = FQDN
            userInfo['port'] = port
            collection.update(searchQuery, userInfo)
            logging.info(u'新用户设置FQDN：%s' % FQDN)
            return True
        else:
            FQDNip = socket.gethostbyname(userInfo['FQDN'])
            logging.info(u'FQDN_IP：%s' % FQDNip)
            if FQDNip == userIp:
                logging.info(u'访问授权')
                return True
            else:
                logging.warning(u'未授权访问,IP不符,用户名：%s , 未授权IP：%s' % (userInfo['user_name'], userIp))
    else:
        logging.warning(u'未授权访问,无此用户,尝试访问IP：' % userIp)
    return False


def addNewUser(userName):
    collection = mongoTools.getCollection('user')
    userUuid = uuid.uuid1()
    user = {
        "user_name": userName,
        "token": userUuid,
        "FQDN": "",
        "port": ""
    }
    collection.insert(user)
    return userUuid
