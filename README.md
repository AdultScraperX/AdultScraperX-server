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
推荐使用我们提供的数据库，本程序使用mongoDB 对每次搜刮结果进行缓存，经过长时间的应用，数据库中已缓存了大量搜刮结果，使用我们提供的数据库可直接使用该缓存加快匹配速度，并避免因为访问量过大被反扒机制屏蔽，如果有能力自行架设数据库也欢迎自行架设
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
```json
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
