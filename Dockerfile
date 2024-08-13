#FROM python:3.10-alpine
#
#RUN apk update && apk upgrade && apk add bash
#RUN apk add --no-cache chromium chromium-chromedriver tzdata
#
#RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
#RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-2.30-r0.apk
#RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.30-r0/glibc-bin-2.30-r0.apk
#
#RUN apk update && apk add --no-cache \
#    openjdk11-jre \
#    bash \
#    wget \
#    graphviz \
#    libc6-compat


# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg2 \
    libnss3 \
    libgconf-2-4 \
    libxi6 \
    libxrender1 \
    libxtst6 \
    xdg-utils \
    libx11-xcb1 \
    libxcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libxss1 \
    libxxf86vm1 \
    libasound2 \
    fonts-liberation \
    libappindicator1 \
    libnss3 \
    libxss1 \
    libappindicator3-1 \
    libindicator7 \
    ca-certificates \
    --no-install-recommends

# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb || apt-get -f install -y \
    && rm google-chrome-stable_current_amd64.deb

# Install chromedriver
RUN CHROME_DRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) \
    && wget https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/local/bin/chromedriver \
    && chmod +x /usr/local/bin/chromedriver \
    && rm chromedriver_linux64.zip

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
