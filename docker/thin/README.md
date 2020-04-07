# 此项目需要国际网络环境请自行解决！
## TG群：https://t.me/AdultScraperX

## Docker for Synology 
### 简述：

```
注：
以下三个插件参数仅在有安装MongoDB4缓存库情况下并且在服务端的config.py中，USER_CHECK=True 时才发挥作用。
因此群晖Docker镜像用户群体无法使用缓存库功能。若需要缓存库功能或者需要开启用户认证那你必须要用另一种方式构建项目，
并且需要同时安装或启用你的MongoDB4,同时你还要根据github上的说明创建MongoDB4的表结构

群辉版Docker服务端没有缓存库功能，因此在plex插件中你无需设置下列字段的设置
1. 个人DDNS
2. Plex端口
3. 令牌
```

### 从Docker中部署AdultScraperX-Server
1. 在Docker套件中选择 注册表
2. 在注册表搜索栏中输入 AdultScraperX 并查找
3. 下载 adultscraperx/adultscraperx-server-thin 镜像
4. 在映像中 创建 adultscraperx/adultscraperx-server-thin 的容器
5. 按需 勾选 【使用高权限执行容器 与 启用资源限制】
6. 点击高级设置按钮
7. 点击端口设置选项菜单
8. 添加端口
- 容器端口设置为:9999
- 本地端口设置为:9999 或 从1-65535其中挑选一个未被占用的端口
9. 点击应用
10. 点击下一步
11. 点击应用

### 其他方式构建项目
[https://github.com/AdultScraperX/AdultScraperX-server](https://github.com/AdultScraperX/AdultScraperX-server)
