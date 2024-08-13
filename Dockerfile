FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    gnupg2 \
    dirmngr \
    ca-certificates \
    openjdk-11-jre-headless \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for Java
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Verify the installation
RUN java -version

# Set the Allure version as an environment variable
ENV ALLURE_VERSION=2.20.1

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
