# AdultScraperX-server-docker
AdultScraperX-server-docker  
### TG群：https://t.me/AdultScraperX

## 使用docker 和 docker-compose 构建 AdultScraperX-server  
### 安装docker（如果已安装可跳过）
CentOS
```
sudo yum install -y yum-utils device-mapper-persistent-data lvm2  
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install -y docker-ce
```
Ubuntu
```
sudo apt-get update  
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu artful stable"  
sudo apt-get update  
sudo apt-get install -y docker-ce
```
设置docker服务启动并开机自启
```
systemctl start docker  
systemctl enable docker  
```
## 安装docker-compose（如果已安装可跳过）
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o   /usr/local/bin/docker-compose  
sudo chmod +x /usr/local/bin/docker-compose
```
## 安装 git （如果已安装可跳过）
Centos 
```
yum install -y git
```
Ubuntu 
```
sudo apt install git
```
clone 并启动项目
```
git clone https://github.com/AdultScraperX/AdultScraperX-server-docker.git  
cd AdultScraperX-server-docker  
docker-compose up -d
```
初始化数据库
```
docker exec -it adultscraperx-mongo-db bash
mongo 127.0.0.1:27017/admin -u root -p adultscraperx
use adultscraperx
db.createUser({user:"adultscraperx",pwd:"adultscraperx",roles:[{role:"readWrite",db:"adultscraperx"}]})
db.createCollection("meta_cache");
db.createCollection("user");
exit
exit
docker-compose restart
```
