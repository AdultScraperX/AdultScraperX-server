FROM python:3.7

# install google chrome and drive
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get -y update \
    && apt-get install -y google-chrome-stable git \
    &&  apt-get install -yqq unzip \
    && wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ \

# set display port to avoid crash
ENV DISPLAY=:99

# install python packegs
RUN pip install --upgrade pip \
    && pip install selenium \
    && pip install lxml \
    && pip install image \
    && pip3 install pillow \
    && pip install requests \
    && pip install pymongo \
    && pip install flask

RUN useradd -ms /bin/bash adultScraperX
WORKDIR  /home/adultScraperX
RUN cd /home/adultScraperX \
    && git clone --depth=1 https://github.com/chunsiyang/AdultScraperX-server.git AdultScraperX-server/ \
    && mv AdultScraperX-server/docker/thin/config.py AdultScraperX-server/config/config.py
USER adultScraperX
CMD python3 AdultScraperX-server/main.py
