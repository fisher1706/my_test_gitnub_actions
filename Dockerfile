FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

#RUN apk update && apk add --no-cache \
#    openjdk11-jre \
#
#
#ENV ALLURE_VERSION=2.14.0
#
#RUN wget https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.tgz && \
#    tar -zxvf allure-${ALLURE_VERSION}.tgz && \
#    mv allure-${ALLURE_VERSION} /opt/allure-${ALLURE_VERSION} && \
#    ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/local/bin/allure
#
#RUN allure --version

WORKDIR ./usr/workspace

VOLUME /usr/workspace

COPY requirements.txt .

RUN pip install --no-cache-dir --verbose -r requirements.txt

COPY . .
