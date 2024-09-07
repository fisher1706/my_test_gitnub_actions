FROM python:3.10-bullseye

RUN apk update && apk upgrade && apk add bash

# Install Chromium, ChromeDriver, and other dependencies
RUN apk update && apk add --no-cache \
    chromium \
    chromium-chromedriver \
    harfbuzz \
    nss \
    freetype \
    ttf-freefont \
    bash

# Set environment variables for Chromium
ENV CHROME_BIN=/usr/bin/chromium-browser \
    CHROME_PATH=/usr/lib/chromium/

# Add Chromium to PATH
ENV PATH=$PATH:/usr/lib/chromium/

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

