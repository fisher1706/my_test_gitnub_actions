FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the Allure version as an environment variable
ENV ALLURE_VERSION=2.20.1

FROM python:3.10-slim

# Install basic utilities and dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends wget openjdk-11-jre-headless unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*



# Download and install Allure command-line tool
RUN wget https://github.com/allure-framework/allure2/releases/download/$ALLURE_VERSION/allure-$ALLURE_VERSION.zip \
    && unzip allure-$ALLURE_VERSION.zip -d /opt/ \
    && ln -s /opt/allure-$ALLURE_VERSION/bin/allure /usr/bin/allure \
    && rm allure-$ALLURE_VERSION.zip

# Verify Allure installation
RUN allure --version

WORKDIR ./usr/workspace

VOLUME /usr/workspace

COPY requirements.txt .

RUN pip install --no-cache-dir --verbose -r requirements.txt

COPY . .
