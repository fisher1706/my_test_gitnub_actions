FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    chromium-driver \
    chromium \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN echo "deb http://deb.debian.org/debian bullseye main" > /etc/apt/sources.list

RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-11-jre-headless \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV ALLURE_VERSION=2.14.0

RUN echo "deb http://deb.debian.org/debian/ bullseye main" > /etc/apt/sources.list

RUN apt-get update && apt-get install -y --no-install-recommends \
    apt-transport-https \
    wget \
    openjdk-11-jre-headless \
    unzip \
    ca-certificates \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/allure-framework/allure2/releases/download/$ALLURE_VERSION/allure-$ALLURE_VERSION.zip \
    && unzip allure-$ALLURE_VERSION.zip -d /opt/ \
    && ln -s /opt/allure-$ALLURE_VERSION/bin/allure /usr/bin/allure \
    && rm allure-$ALLURE_VERSION.zip

RUN allure --version




WORKDIR ./usr/workspace

VOLUME /usr/workspace

COPY requirements.txt .

RUN pip install --no-cache-dir --verbose -r requirements.txt

COPY . .

