#! /usr/bin/env python
# -*- coding: utf-8 -*-
import logging

import base64
import json
import re
import sys
import app.internel.user_tools as userTools
import app.internel.mongo_tools as mongoTools
import config.spider_config as spider_config
import config.config as config

from flask import Flask, request
from flask import render_template
from flask import send_file
from googletrans import Translator


if sys.version.find('2', 0, 1) == 0:
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO
else:
    from io import StringIO
    from io import BytesIO

# 必填且与plex对应

app = Flask(__name__)


@app.route("/")
@app.route("/index")
@app.route("/warning")
def warning():
    beta = {'beta': '1.2.2'}
    return render_template(
        'warning.html',
        **beta
    )


@app.route('/t/<dirTagLine>/<tran>')
def t(dirTagLine, tran):

    data = base64.b64decode(tran.replace(';<*', '/')).decode("utf-8")
    translator = Translator()
    if not data == '':
        try:
            logging.info("执行翻译")
            if dirTagLine == 'censored' or dirTagLine == 'uncensored' or dirTagLine == 'animation':
                data = translator.translate(data,  src='ja', dest='zh-cn').text

            if dirTagLine == 'europe':
                data = translator.translate(data,  src='en', dest='zh-cn').text
        except Exception as ex:
            Log('翻译出现异常 ：%s' % ex)

    translator = None
    return data


@app.route("/img/<data>/<r>/<w>/<h>")
def img(data, r, w, h):
    data = json.loads(base64.b64decode(data))
    image = None
    for sourceList in spider_config.SOURCE_LIST:
        for sourceItem in spider_config.SOURCE_LIST[sourceList]:
            for spiderClass in sourceItem["webList"]:
                spider = spiderClass()
                if spider.getName().lower() == data['webkey'].lower():
                    if r == 0 and w == 0 and h == 0:
                        image = spider.pictureProcessing(data)
                    else:                
                        image = spider.pictureProcessingCFT(data,r,w,h)
    if image is not None:
        try:
            img_io = StringIO()
            image.save(img_io, 'PNG')
        except Exception:
            img_io = BytesIO()
            image.save(img_io, 'PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/jpg')
    else:
        return ''


@app.route('/addUser/<adminToken>/<username>')
def addUser(adminToken, username):
    if adminToken == config.SERVE_ADMIN_TOKEN:
        return json.dumps({'issuccess': 'true', 'token': userTools.addNewUser(username), 'ex': ''})
    return json.dumps({'issuccess': 'false', 'token': '', 'ex': '未授权访问'})


@app.route('/<requestType>/<dirTagLine>/<q>/<token>/<FQDN>/<port>')
def getMediaInfos(requestType, dirTagLine, q, token, FQDN, port):
    """
    根据搜刮网站列表进行数据搜刮
    :param cacheFlag: 使用缓存标识
    :param webList: 搜刮网站的List 类型应为 app.spider.BasicSpider 的子类
    :param q: 待匹配的文件名
    :param autoFlag: 自动表示 True 为开启，开启后仅返回搜索到的第一个结果 ，False 为关闭
    :return:
        未查询到example
        {
            'issuccess': 'false',
            'json_data': [],
            'ex': ''
        }
        查询到
        {
            'ex':'', // 异常信息
            'issuccess':'true', //返回数据状态 true or false
            'json_data': [ // 数据集(可包含有多个站点的数据)
                {
                'sitName': { //站点名称
                    'm_actor': { // 演员集
                            '': '' // 名称：url 路径 需包含http或https头
                    },
                    'm_art_url':'', // plex背景图
                    'm_category':'', // 类型 多个以 , 分开
                    'm_collections':'', // 系列 多个以 , 分开
                    'm_directors':'', //导演 多个以 , 分开
                    'm_id':'', // 影片id（不需要填写）
                    'm_number':'', // 番号,此项为必填项
                    'm_originallyAvailableAt':'', // 上映日期 yyyy-MM-dd
                    'm_poster':'', //海报url  需包含 http或https头
                    'm_studio':'', // 工作室,出品方 多个以 , 分开
                    'm_summary':'', // 概述
                    'm_title':'', //标题,此项为必填项
                    'm_year':'' //年份 yyyy-MM-dd

                    }
                }
            ]
        }
    """
    if token == '':
        return 'T-Error!'

    logging.info(u'======开始请求======')

    q = base64.b64decode(q.replace('[s]', '/')).decode("utf-8")
    # 检查服务端状态
    if q == '--checkState':
        return checkState(token, FQDN, port)
    # 检查搜刮器状态
    if q == '--checkSpider':
        return checkSpider()

    userIp = request.remote_addr
    if config.THIN_MODE is False and \
            config.USER_CHECK is True and \
            not userTools.checkUser(token, userIp, FQDN, port):
        logging.info(u'======请求结束======')
        return 'T-Error!'

    if requestType == "manual":
        logging.info(u'模式：手动')
        autoFlag = False
    elif requestType == "auto":
        logging.info(u'模式：自动')
        autoFlag = True
    else:
        return 'URL-Error!'

    logging.info(u'文件名：%s' % q)
    logging.info(u'目录标记：%s' % dirTagLine)
    cacheFlag = True
    if q.find(config.CacheTag) > -1:  # 判断是否跳过缓存数据库
        logging.info(u'手动强制输入命令%s跳过使用缓存库' % config.CacheTag)
        cacheFlag = False
        q = q.replace(config.CacheTag, '')
    if dirTagLine != "" or not spider_config.SOURCE_LIST[dirTagLine]:
        # 初始化绕过正则判断变量
        nore = False
        for template in spider_config.SOURCE_LIST[dirTagLine]:
            # 循环模板列表
            codeList = []
            if q.find(config.NotUseRe) > -1:
                #q = q.replace(config.NotUseRe, '')
                # 设置绕过正则变量
                nore = True
                re_list = re.finditer(
                    r'.+', q.replace(config.NotUseRe, ''), re.IGNORECASE)
            else:
                re_list = re.finditer(template['pattern'], q.replace(
                    config.NotUseRe, ''), re.IGNORECASE)

            for item in re_list:
                codeList.append(item.group())

            while '' in re_list:
                re_list.remove('')

            if len(codeList) == 0:
                continue
            # 对正则匹配结果进行搜索
            for code in codeList:
                # 判断绕过正则
                if nore:
                    items = search(template['webList'],
                                   code, autoFlag, cacheFlag)
                else:
                    items = search(template['webList'],
                                   template['formatter'].format(code),
                                   autoFlag,
                                   cacheFlag)

                if items.get("issuccess") == "true":
                    logging.info("匹配数据结果：success")
                    logging.info(u'======结束请求======')
                    logging.info(u'======返回json======')
                    return json.dumps(items)
                else:
                    logging.info("匹配数据结果：未匹配到结果")

    logging.info(u'======结束请求======')
    logging.info(u'======返回json======')
    return json.dumps({'issuccess': 'false', 'json_data': [], 'ex': ''})


def search(webList, q, autoFlag, cacheFlag=False):
    logging.info("格式化后的查询关键字：%s" % q)
    result = {
        'issuccess': 'false',
        'json_data': [],
        'ex': ''
    }
    for webSiteClass in webList:
        webSite = webSiteClass()
        if cacheFlag and config.THIN_MODE is False:
            items = webSite.searchWithCache(q, webSite.getName())
        else:
            items = webSite.search(q)

        for item in items:
            if item['issuccess']:
                result.update({'issuccess': 'true'})
                result['json_data'].append({webSite.getName(): item['data']})
                logging.info("匹配关键字：%s  元数据来源站点：%s" % (q, webSite.getName()))
                if autoFlag:
                    return result
    return result


def checkState(token, FQDN, port):
    resultDate = []
    resultDate.append(setCheckState('1', '服务端版本' + str(config.SERVER_VERSION)))
    # 数据库检测
    resultDate.append(setCheckState('2', '数据库检测'))
    if config.THIN_MODE is True:
        resultDate.append(setCheckState('2.1', '精简模式跳过数据库检测'))
    else:
        try:
            mongoTools.getConnection()
            resultDate.append(setCheckState('2.1', '数据库链接创建成功'))
            try:
                mongoTools.getDatabase()
                resultDate.append(setCheckState('2.2', '数据库登陆成功'))
                try:
                    mongoTools.getCollection('meta_cache')
                    resultDate.append(setCheckState('2.3', '数据库用户权限设置正确'))
                except Exception:
                    resultDate.append(setCheckState(
                        '2.1', '数据库用户权限设置不正确，请检查用户权限'))
            except Exception:
                resultDate.append(setCheckState('2.2', '数据库登陆失败，请检测用户名密码'))
        except Exception:
            resultDate.append(setCheckState(
                '2.3', '数据库链接创建失败，请检查服务器是否启动及地址是否正确'))

    # 用户检测
    if config.THIN_MODE is True or config.USER_CHECK is True:
        resultDate.append(setCheckState('3', '用户检测'))
        if userTools.checkUser(token, request.remote_addr, FQDN, port):
            resultDate.append(setCheckState(
                '3.1', 'token:' + token + ', FQDN:' + FQDN + '用户为授权用户'))
        else:
            resultDate.append(setCheckState(
                '3.1', 'token:' + token + ', FQDN:' + FQDN + '用户为非授权用户'))

    result = {'issuccess': 'true', 'json_data': resultDate, 'ex': ''}
    return json.dumps(result)


def checkSpider():
    resultDate = []
    resultDate.append(setCheckState('日本有码', '搜刮器检测'))
    checkSpiderConnection('censored', resultDate)
    resultDate.append(setCheckState('日本无码', '搜刮器检测'))
    checkSpiderConnection('uncensored', resultDate)
    resultDate.append(setCheckState('动漫搜刮', '搜刮器检测'))
    checkSpiderConnection('animation', resultDate)
    resultDate.append(setCheckState('欧美搜刮', '搜刮器检测'))
    checkSpiderConnection('europe', resultDate)

    result = {'issuccess': 'true', 'json_data': resultDate, 'ex': ''}
    return json.dumps(result)


def checkSpiderConnection(type, resultDate):
    for spiderType in spider_config.SOURCE_LIST[type]:
        for spider in spiderType['webList']:
            spiderObj = spider()
            resultDate.append(setCheckState(
                spiderType['name']+':' + spiderObj.getName(), '可连接' if spiderObj.checkServer() else '不可连接'))


def setCheckState(number, title):
    return {
        '': {
            'm_id': '',
            'm_number': number,
            'm_title': title,
            'm_poster': '',
            'm_art_url': '',
            'm_summary': 'CheckState',
            'm_studio': 'CheckState',
            'm_directors': 'CheckState',
            'm_collections': 'CheckState',
            'm_year': '',
            'm_originallyAvailableAt': '',
            'm_category': 'CheckState',
            "m_actor": ''
        }

    }


if __name__ == "__main__":
    app.run(
        host=config.HOST,
        port=config.PORT,
        debug=config.DEBUG
    )
