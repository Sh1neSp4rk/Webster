# framework/config.py

import os
import pytz
from dotenv import load_dotenv
from datetime import datetime, timedelta
import time

class Config:
    def __init__(self):
        load_dotenv()  # Ensure .env is loaded

        # Email settings
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.target_email = os.getenv("TARGET_EMAIL")

        # Directories for downloads and screenshots
        self.download_dir = os.getenv("DOWNLOAD_DIR", "downloads")  
        self.screenshot_dir = os.getenv("SCREENSHOT_DIR", "screenshots")  

        # Timezone settings
        self.timezone = pytz.timezone("America/Toronto")

        # Retry settings for element interaction
        self.retry_count = int(os.getenv("RETRY_COUNT", 3))  # Default to 3 retries
        self.retry_wait_time = int(os.getenv("RETRY_WAIT_TIME", 2))  # Wait time between retries in seconds

    # --- Directory Methods ---
    def get_download_dir(self):
        """Returns the download directory."""
        return self.download_dir

    def get_screenshot_dir(self):
        """Returns the screenshot directory."""
        return self.screenshot_dir

    # --- Time and Date Methods ---
    def now(self):
        """Returns the current time in the configured timezone."""
        return datetime.now(self.timezone)

    def format_date(self, days_offset=0, date_format="%Y-%m-%d"):
        """
        Returns a formatted date string offset by a given number of days.
        :param days_offset: Days to add/subtract from today's date
        :param date_format: Format string for the output date
        :return: Formatted date as string
        """
        target_date = datetime.now(self.timezone) + timedelta(days=days_offset)
        return target_date.strftime(date_format)

    def sleep(self, seconds):
        """Pauses execution for a given number of seconds."""
        time.sleep(seconds)

# Initialize a global config instance to be used throughout the app
config = Config()
