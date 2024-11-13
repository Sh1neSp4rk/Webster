# framework/logger.py

import os
import logging
from config import config

# Define color codes for console output
COLORS = {
    "DEBUG": "\033[35m",    
    "INFO": "\033[94m",     
    "WARNING": "\033[93m",  
    "ERROR": "\033[91m",    
    "CRITICAL": "\033[31m", 
    "RESET": "\033[0m"      
}

SCREENSHOT_DIR = config.screenshot_dir
screenshot_counter = threading.local()  # Use threading.local for thread-safe counter

# Initialize the root logger
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()  # This gets the root logger

class CustomFormatter(logging.Formatter):
    def __init__(self, driver=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.driver = driver

    def format(self, record):
        color = COLORS.get(record.levelname.strip("\033"), COLORS["RESET"])
        record.levelname = f"{color}{record.levelname}{COLORS['RESET']}"
        return super().format(record)

def setup_logging(log_file='logs/app.log', driver=None):
    """Sets up logging with both file and console handlers."""
    # Ensure log directory exists
    log_dir = os.path.dirname(log_file)
    os.makedirs(log_dir, exist_ok=True)

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)  # This adds the file handler to the root logger

    # Console handler
    console_handler = logging.StreamHandler()
    console_formatter = CustomFormatter(driver=driver, fmt='%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)  # This adds the console handler to the root logger

    logger.info(f"Logging set up. Logs will be written to: {log_file}")

def write_ascii_header(log_file):
    header = "NEW SCRIPT EXECUTION"
    total_width = 55
    timestamp = config.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, 'a') as log:
        log.write("\n" + "*" * total_width + "\n")
        log.write(f"* {header.center(total_width - 4)} *\n")
        log.write("*" * total_width + "\n")
        log.write(f"Execution started at: {timestamp}\n")
        log.write("*" * total_width + "\n")

    return header

def trim_log_file(log_file, header, max_runs=5):
    """Trims the log file to retain only the last few runs."""
    if not os.path.exists(log_file):
        return

    with open(log_file, 'r') as f:
        lines = f.readlines()

    run_indices = [i for i, line in enumerate(lines) if header in line]

    if len(run_indices) > max_runs:
        start_index = run_indices[-max_runs]
        lines = lines[start_index:]

        with open(log_file, 'w') as f:
            f.writelines(lines)

def get_screenshot_counter():
    """Thread-safe increment of screenshot counter."""
    if not hasattr(screenshot_counter, 'counter'):
        screenshot_counter.counter = 1
    else:
        screenshot_counter.counter += 1
    return screenshot_counter.counter

def take_screenshot(driver, step_name: str, logger) -> None:
    """Takes a screenshot and logs the path, incrementing the counter."""
    timestamp = config.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

    screenshot_number = f"{get_screenshot_counter():02d}"
    screenshot_path = os.path.join(SCREENSHOT_DIR, f"{screenshot_number}_{step_name}_{timestamp}.png")

    try:
        driver.save_screenshot(screenshot_path)
        logger.info(f"Screenshot taken: {screenshot_path}")
    except Exception as e:
        logger.error(f"Failed to take screenshot at {screenshot_path}: {e}", exc_info=True)

def delete_all_screenshots() -> None:
    """Deletes all screenshots in the specified directory."""
    global logger  # Access the global logger
    try:
        if os.path.exists(SCREENSHOT_DIR):
            files_deleted = 0
            for filename in os.listdir(SCREENSHOT_DIR):
                file_path = os.path.join(SCREENSHOT_DIR, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    files_deleted += 1
            if files_deleted:
                logger.debug(f"Deleted {files_deleted} screenshots in {SCREENSHOT_DIR}")
            else:
                logger.info(f"No screenshots to delete in {SCREENSHOT_DIR}")
    except Exception as e:
        logger.error(f"Failed to delete screenshots in {SCREENSHOT_DIR}: {e}", exc_info=True)
