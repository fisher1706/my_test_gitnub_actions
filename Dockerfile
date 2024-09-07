# Use a base image with JDK and Maven if you plan to run tests with Java
FROM openjdk:11-jdk-slim

# Install dependencies like curl, gnupg, unzip, etc.
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gnupg \
    unzip \
    xvfb \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Add Google's signing key and repository
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-linux-keyring.gpg \
    && echo "deb [signed-by=/usr/share/keyrings/google-linux-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google-chrome.list

# Install Chrome
RUN apt-get update \
    && apt-get install -y google-chrome-stable --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Install ChromeDriver
RUN CHROME_DRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) \
    && wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip \
    && chmod +x /usr/local/bin/chromedriver

# Install Allure
RUN wget -O /tmp/allure.zip https://github.com/allure-framework/allure2/releases/download/2.17.2/allure-2.17.2.zip \
    && unzip /tmp/allure.zip -d /opt/ \
    && ln -s /opt/allure-2.17.2/bin/allure /usr/bin/allure

# Set environment variables for Chrome and ChromeDriver
ENV DISPLAY=:99
ENV CHROME_BIN=/usr/bin/google-chrome

WORKDIR ./usr/workspace

VOLUME /usr/workspace

COPY requirements.txt .

RUN pip install --no-cache-dir --verbose -r requirements.txt

COPY . .

