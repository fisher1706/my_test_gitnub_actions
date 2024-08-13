FROM python:3.10-alpine

RUN apk update && apk upgrade && apk add bash

#FROM joyzoursky/python-chromedriver:3.8-alpine3.10-selenium
# install system dependencies
RUN apk add linux-headers
RUN apk update && apk add --no-cache --repository=http://dl-cdn.alpinelinux.org/alpine/edge/testing
RUN apk add --no-cache gcc g++ git openssh-client
RUN apk add --no-cache python3-dev openssl-dev libffi-dev gcc musl-dev && pip3 install --upgrade pip
# env vars for selenium
ENV DISPLAY=':99'
ENV CHROME_DRIVER=/usr/bin/chromedriver

WORKDIR /root
RUN mkdir .ssh
RUN chmod 700 .ssh

RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-bin-2.30-r0.apk

RUN apk update && apk add --no-cache \
    openjdk11-jre \
    bash \
    wget \
    graphviz \
    libc6-compat

ENV ALLURE_VERSION=2.14.0

RUN wget https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.tgz && \
    tar -zxvf allure-${ALLURE_VERSION}.tgz && \
    mv allure-${ALLURE_VERSION} /opt/allure-${ALLURE_VERSION} && \
    ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/local/bin/allure

RUN allure --version

WORKDIR ./usr/workspace

VOLUME /usr/workspace

COPY requirements.txt .

RUN pip install --no-cache-dir --verbose -r requirements.txt

COPY . .
