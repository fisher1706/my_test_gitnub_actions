FROM python:3.10-alpine

RUN apk update && apk upgrade && apk add bash

# Install dependencies
RUN apk --no-cache add \
    chromium \
    chromium-chromedriver \
    harfbuzz \
    nss \
    freetype \
    ttf-freefont \
    font-noto \
    wqy-zenhei \
    libstdc++ \
    libx11 \
    libxcb \
    libxcomposite \
    libxrandr \
    libxi \
    dbus \
    ttf-dejavu

# Set environment variables to ensure Chromium runs properly
ENV CHROME_BIN=/usr/bin/chromium-browser \
    CHROMEDRIVER_BIN=/usr/bin/chromedriver

# Make sure you can use Chromium and Chromedriver
RUN chromium-browser --version && chromedriver --version

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
