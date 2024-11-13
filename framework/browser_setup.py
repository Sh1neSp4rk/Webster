# framework/browser_setup.py

import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config import config  # Import the config instance

logger = logging.getLogger(__name__)

def create_chrome_driver() -> webdriver.Chrome:
    """
    Sets up and returns a headless Chrome WebDriver with download settings.
    
    Returns:
        webdriver.Chrome: Configured Chrome driver, or None if driver setup fails.
    """
    logger.debug("Setting up Chrome driver with headless options")
    
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": config.download_dir,  # Use config for download directory
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    except Exception as e:
        logger.error(f"Failed to create Chrome driver: {e}")
        return None

    logger.debug("Chrome driver setup complete")
    return driver
