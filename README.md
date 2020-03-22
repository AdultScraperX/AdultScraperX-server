# 此项目需要国际网络环境请自行解决！
# AdultScraperX-server 服务端

这是一个可以匹配成人影片信息的插件服务端（不提供任何影片下载与观看连接），仅提供简介，演员，标题，类型，系列，导演，工作室的信息匹配。

### TG群：https://t.me/AdultScraperX

# 部署及配置部分
## 服务端配置说明
- 服务端配置文件为 `app/confog/config.py`    

## 插件地址 
- https://github.com/chunsiyang/AdultScraperX.bundle

## 如果你是linux小白，只会用群晖，可以使用如下精简版安装，将极大程度减少安装复杂度，强烈建议小白使用
- https://github.com/chunsiyang/AdultScraperX-server/tree/master/docker/thin

## 推荐使用docker部署本项目详情请参考  
- https://github.com/chunsiyang/AdultScraperX-server-docker  

## 独立部署项目（不推荐，需要自行提供MongoDB4数据库）
1. 配置数据库  
```
MONGODB_HOST = 'mongohost'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'adultscraperx'
MONGODB_USER = 'adultscraperx'
MONGODB_PWD = 'adultscraperx'
```

2. 用户认证设置  
`USER_CHECK = False`  
默认关闭用户认证，开启用户认证后只有携带正确 Token 并且 FQDN 正确的用户可以访问服务器，建议服务端和插件通过公网链接的用户开启此选项

3. 选择浏览器驱动，支持 ‘firefox’ 和 ‘chrome’  
```
BROWSER_DRIVE = 'chrome'
```

## 部署说明
 以 Linux CentOS 为例 windows及其他平台请自行查找安装教程
### clone 项目
```linux
git clone https://github.com/chunsiyang/AdultScraperX-server.git
cd AdultScraperX-server
```
### 安装python
```
yum install -y python37
yum install -y epel-release
yum install -y python3-pip
yum install -y git
```
### pip安装类包
```linux
pip3 install image 
pip3 install pillow
pip3 install lxml 
pip3 install requests
pip3 install pymongo 
pip3 install selenium
pip3 install flask 
pip3 install googletrans
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

### 对于自行建立MongoDB4数据库的用户请使用如下建库脚本
- 请自行安装MongoDB4,并创建数据库用户及密码
- 下列只给出如何创建数据库
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
## 影片信息搜刮工作流程说明
在收到plex插件请求后，根据插件提供的分类信息（日本无码，日本有码，欧美，动漫）选择 config.py 中 SOURCE_LIST 下配置的搜刮器信息列表。  
循环搜刮器信息列表并使用其中配置的正则进行匹配，如果正则匹配成功则调用 formater 进行名称格式化获得纯净的番号，并将格式化后的番号传送给 spider 进行数据搜刮
## 新刮刀（spider）添加说明
### 如何创建新的刮刀（spider）
#### 什么是刮刀（spider）
1. 刮刀的意思就是将一个网站内所需要的信息收录因此成为刮刀，或者你可以叫它 spider、爬虫之类的 总之就是收录信息为目的的行为。
2. 刮刀在这里只做一些基础常规的事情，你只需要让他获取媒体信息中相对应的信息即可。
3. 这里有固定需要的到的信息，可以从[插件与server通信接口说明](#插件与server通信接口说明) 了解到你所需要得到的内容。
4. 在创作刮刀时请选择长久稳定的信息提供者，这有助于刮刀以更长的生命周期运行。
### 创建 一个新的 spider
- 这里的负责的工作是进行信息的收录工作，将站点的信息进行收录并解析成需要的媒体信息。
1. spider类位于app/spider/目录下
2. 创建一个 spider 类 命名规范：站点名称.py
例：google.py
3. 我们提供了basic_spider 的基类，封装了常用方法，所有spider需要继承该类或其子类，并实现其中声明必须实现的接口和必须赋值的变量 
4. 类参考
日本有码站点确认访问功能的：参考 arzon.py 代码
日本无码站点确认访问功能的：参考 javbus.py 代码
需要模拟无头浏览器的：参考 mgstage.py 代码
完整海报剪切：参考 arzon.py 代码
缩放比例海报：参考 mgstage.py 代码

### 创建 一个新的 formatter

- 这里负责的工作是格式化番号，将略有规则的番号格式化成所需要使用的格式。
1. formatter类位于app/formatter/目录下
2. 创建一个 formatter 类 命名规范：站点名称Formatter.py
例：basicFormatter.py
3. 参考类
请参考 formatter 目录下的任何类

#### 向spider_config.py添加一个新的刮刀
- 这里负责的工作是将创建好的 formatter、spider类引用，使其能够正常被调用工作。
- 刮刀信息存储在spider_config.py SOURCE_LIST中，并以日本无码，日本有码，欧美，动漫，进行了分类
- 格式说明
```
{
    "name": '10musume', #搜刮的类型说明，str类型
    "pattern": r"\d{6}.\d{3}", #正则表达式
    'formatter': TenMusumeFormatter, #格式化器
    'webList': [TenMusume, Javr] #搜刮器，可以为多个
}
```
1. spider_config.py位于 根目录下
2. 追加spider_config.py的内容
3. 先要from import 你的新formatter、spider类
4. 在SOURCE_LIST内对应追加操作
5. 添加搜刮器时按照对应的分类添加到对应的列表中

#### 系统配置 config.py 
- config.py存放着一些有关于全局的配置变量,在为运行时你可以修改他,一旦运行将不可改变。

# 常见服务器异常log输出
## 以下请找自身网络问题：
### error : ConnectionError(ProtocolError('Connection aborted.', OSError(0, 'Error')))
- 网络连接断开或无法连接
### Errno 111
- 拒绝连接
### Errno 110
- 检查你的服务端是否启动

## 程序抛异常怎么办？
### Issues上报
- Issues 上报问题 阐述问题并使用  \`\`\` 你的最新日志文本 \`\`\` 发表Issues （不要上传任何文件）
### 以下是程序报错例子
- 通常程序错误会出现类似于下面的内容
```
Traceback (most recent call last):
  File "/usr/local/lib/python3.7/site-packages/flask/app.py", line 2446, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/local/lib/python3.7/site-packages/flask/app.py", line 1951, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/local/lib/python3.7/site-packages/flask/app.py", line 1820, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/local/lib/python3.7/site-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/usr/local/lib/python3.7/site-packages/flask/app.py", line 1949, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/local/lib/python3.7/site-packages/flask/app.py", line 1935, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "AdultScraperX-server/main.py", line 200, in getMediaInfos
    cacheFlag)
  File "AdultScraperX-server/main.py", line 227, in search
    items = webSite.search(q)
  File "/home/adultScraperX/AdultScraperX-server/app/spider/arzon.py", line 63, in search
    html_item['html'], q)
  File "/home/adultScraperX/AdultScraperX-server/app/spider/arzon.py", line 93, in analysisMediaHtmlByxpath
    title = html.xpath(xpath_title)
AttributeError: 'NoneType' object has no attribute 'xpath'
```



