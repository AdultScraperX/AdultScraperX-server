# AdultScraperX-server 服务端
Plex 成人影片搜刮器AdultScraperX的服务端
# 部署及配置部分
## 服务端配置说明
服务端配置文件为 `config.py`    

1. 配置数据库  
```
MONGODB_HOST = 'mineserver.top'
MONGODB_PORT = 50000
MONGODB_DBNAME = 'adultscraperx'
MONGODB_USER = 'adultscraperx'
MONGODB_PWD = 'adultscraperx'
```  
推荐使用官方提供的数据库，本程序使用mongoDB 对每次搜刮结果进行缓存，经过长时间的应用，数据库中已缓存了大量搜刮结果，使用官方提供的数据库可直接使用该缓存加快匹配速度，并避免因为访问量过大被反扒机制屏蔽，如果有能力自行架设数据库也欢迎自行架设  

2. 用户认证设置  
`USER_CHECK = True`  
默认开启用户认证，只有携带正确 Token 并且 FQDN 正确的用户可以访问服务器，设置为 False 以关闭此功能  
\* 使用官方数据库请将此选项设置为False
## 部署说明
 以 Linux CentOS 为例 windows及其他平台请自行查找安装教程
### clone 项目
```linux
git clone https://github.com/chunsiyang/AdultScraperX-server.git
cd AdultScraperX-server
```
### 安装python
`yum install python37`
### pip安装类包
```linux
pip install image
pip install lxml
pip install requests
pip install pymongo
pip install selenium
pip install flask
```

### 安装firfox浏览器及驱动
1. 安装Firfox
```
yum -y install firefox
```
2. 解压浏览器驱动(驱动在项目中可找到)
```
tar -zxvf geckodriver-v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
mv geckodriver-v0.26.0/geckodriver /usr/bin
```
### 运行
`python3 ./main.py`

### 对于自行建立数据库的用户请使用如下建库脚本
```
db.getCollection("meta_cache").drop();
db.createCollection("meta_cache");
db.getCollection("user").drop();
db.createCollection("user");
```
# 接口说明及新刮刀添加说明
## 插件与server通信接口说明
plex 影片搜刮分为自动搜刮和手动匹配，这两种方式的匹配都将由main.py中的 getMediaInfos 方法响应，该方法与plex通信的json格式如下
```
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
```
## 新刮刀添加说明
### 如何创建新的刮刀
#### 什么是刮刀
1. 刮刀的意思就是将一个网站内所需要的信息收录因此成为刮刀，或者你可以叫它 spider、爬虫之类的 总之就是收录信息为目的的行为。
2. 刮刀在这里只做一些基础常规的事情，你只需要让他获取媒体信息中相对应的信息即可。
3. 这里有固定需要的到的信息，可以从 [插件与server通信接口说明](#插件与server通信接口说明) 了解到你所需要得到的内容。
4. 在创作刮刀时请选择长久稳定的信息提供者，这有助于刮刀以更长的生命周期运行。
5. 请保证你收录的信息中没有额外的信息出现，请不要擅自加入广告，因为它不受欢迎，我们也不希望看到广告。请保证你的收录的信息整洁。
#### 创建 一个新的 spider
- 这里的负责的工作是 进行信息的收录工作，将站点的信息进行收录并解析成需要的媒体信息。
1. spider类位于app/spider/目录下
2. 创建一个 spider 类 命名规范：站点名称.py
例：google.py
3. 基本操作类 basic_spider.py  看注解进行参考使用 你可以直接引用但我们不建议你做任何的修改以免造成未知问题。
4. 类参考
有站点确认访问功能的：参考 arzon.py 代码
无站点确认访问功能的：参考 javbus.py 代码
需要模拟无头浏览器的：参考 mgstage.py 代码
完整海报剪切：参考 arzon.py 代码
缩放比例海报：参考 mgstage.py 代码
## 创建 一个新的 formatter
- 这里负责的工作是格式化番号，将略有规则的番号格式化成所需要使用的格式。
1. formatter类位于app/formatter/目录下
2. 创建一个 formatter 类 命名规范：站点名称Formatter.py
例：basicFormatter.py
3. 参考类
请参考 formatter 目录下的任何类

#### 向config添加一个新的刮刀
- 这里负责的工作是将创建好的 formatter、spider类引用，使其能够正常被调用工作。
1. config.py位于 根目录下
2. 追加config.py的内容
3. 先要from import 你的新formatter、spider类
4. 在SOURCE_LIST内对应追加操作
5. 请规范追加切勿破坏整体构造
