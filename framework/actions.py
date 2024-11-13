# framework/actions.py

import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logger import take_screenshot
from error_handler import error_handler
from config import config

logger = logging.getLogger(__name__)

@error_handler("Find Element")
def find_element(driver, locator):
    for attempt in range(config.retry_count):
        try:
            element = WebDriverWait(driver, config.retry_wait_time).until(EC.visibility_of_element_located(locator))
            logger.debug(f"Element located at {locator} is now visible.")
            return element
        except Exception:
            if attempt + 1 < config.retry_count:
                logger.info(f"Retrying in {config.retry_wait_time} seconds...")
                config.sleep(config.retry_wait_time)
            else:
                take_screenshot(driver, f"FindElementError_{locator}")
                raise

@error_handler("Click Element")
def click_element(driver, locator):
    for attempt in range(config.retry_count):
        try:
            element = find_element(driver, locator)  # Find the element using the locator
            element.click()
            logger.debug(f"Clicked on element located at {locator}.")
            return
        except Exception:
            if attempt + 1 < config.retry_count:
                logger.info(f"Retrying in {config.retry_wait_time} seconds...")
                config.sleep(config.retry_wait_time)
            else:
                take_screenshot(driver, f"ClickElementError_{locator}")
                raise

@error_handler("Write to Element")
def write_to_element(driver, locator, text):
    for attempt in range(config.retry_count):
        try:
            element = find_element(driver, locator)  # Find the element using the locator
            element.clear()
            element.send_keys(text)
            logger.debug(f"Entered text '{text}' into element located at {locator}.")
            return
        except Exception:
            if attempt + 1 < config.retry_count:
                logger.info(f"Retrying in {config.retry_wait_time} seconds...")
                config.sleep(config.retry_wait_time)
            else:
                take_screenshot(driver, f"WriteElementError_{locator}")
                raise

@error_handler("Navigate to Page")
def navigate(driver, url):
    for attempt in range(config.retry_count):
        try:
            driver.get(url)
            WebDriverWait(driver, 10).until(lambda d: url in d.current_url)
            logger.info(f"Successfully navigated to {url}.")
            return
        except Exception:
            if attempt + 1 < config.retry_count:
                logger.info(f"Retrying in {config.retry_wait_time} seconds...")
                config.sleep(config.retry_wait_time)
            else:
                take_screenshot(driver, f"NavigateError_{url}")
                raise
