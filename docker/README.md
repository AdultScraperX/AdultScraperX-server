# AdultScraperX-server-docker
AdultScraperX-server-docker  
##使用docker 和 docker-compose 构建 AdultScraperX-server  
### 安装docker（如果已安装可跳过）
CentOS
```
sudo yum install -y yum-utils \  
  device-mapper-persistent-data \  
  lvm2  
sudo yum-config-manager \  
    --add-repo \  
    https://download.docker.com/linux/centos/docker-ce.repo  
```
Ubuntu
```
sudo apt-get update  
sudo apt-get install \  
    apt-transport-https \  
    ca-certificates \  
    curl \  
    gnupg-agent \  
    software-properties-common  
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -  
sudo add-apt-repository \  
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \   
   $(lsb_release -cs) \  
   stable"  
sudo apt-get update  
sudo apt-get install docker-ce docker-ce-cli containerd.io  
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
yum install git
```
Ubuntu 
```
sudo apt install git
```
clone 并启动项目
```
git clone https://github.com/chunsiyang/AdultScraperX-server-docker.git  
cd AdultScraperX-server-docker  
docker-compose up -d
```
