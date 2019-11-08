import logging
import socket

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
        logging.debug(u'用户访问IP：%s' % userIp)
        if userInfo['FQDN'] == '':
            userInfo['FQDN'] = FQDN
            userInfo['port'] = port
            collection.update(searchQuery, userInfo)
            logging.debug(u'新用户设置FQDN：%s' % FQDN)
            return True
        else:
            FQDNip = socket.getaddrinfo(FQDN, 'http')[0][4][0]
            logging.debug(u'FQDN_IP：%s' % FQDNip)
            if FQDNip == userIp:
                logging.debug(u'访问授权')
                return True
            else:
                logging.warning(u'未授权访问,IP不符,用户名：%s , 未授权IP：%s' % (userInfo['user_name'],userIp))
    else:
        logging.warning(u'未授权访问,无此用户,尝试访问IP：' % userIp)
    return False
