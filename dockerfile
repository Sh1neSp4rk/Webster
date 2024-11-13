# Use an official Python image as a base
FROM python:3.10-slim

# Set up environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY setup/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install additional system dependencies for Chrome, ChromeDriver, Firefox, and GeckoDriver
RUN apt-get update && \
    apt-get install -y wget gnupg unzip && \
    # Install Google Chrome
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    # Install ChromeDriver
    wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$(wget -q -O - https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin && \
    rm /tmp/chromedriver.zip && \
    # Install Firefox
    apt-get install -y firefox && \
    # Install GeckoDriver
    GECKO_DRIVER_VERSION=$(curl -sS https://api.github.com/repos/mozilla/geckodriver/releases/latest | grep 'tag_name' | cut -d '"' -f 4) && \
    wget https://github.com/mozilla/geckodriver/releases/download/${GECKO_DRIVER_VERSION}/geckodriver-${GECKO_DRIVER_VERSION}-linux64.tar.gz && \
    tar -xzf geckodriver-${GECKO_DRIVER_VERSION}-linux64.tar.gz && \
    mv geckodriver /usr/local/bin/ && \
    rm geckodriver-${GECKO_DRIVER_VERSION}-linux64.tar.gz && \
    # Clean up
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the rest of your code into the container
COPY . /app

# Expose a port if you need access to services
# EXPOSE 8000

# Start command to enter into bash for interactive development
CMD ["bash"]
