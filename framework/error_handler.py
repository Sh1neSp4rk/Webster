# framework/error_handler.py

import logging
from functools import wraps
from selenium.common.exceptions import TimeoutException
from logger import take_screenshot
from pprint import pformat  # For pretty printing the arguments

logger = logging.getLogger(__name__)

def error_handler(context: str):
    """Decorator to handle errors in a function."""
    def decorator(func):
        @wraps(func)
        def wrapper(driver, *args, **kwargs):
            try:
                return func(driver, *args, **kwargs)
            except Exception as e:
                # Create a detailed error message
                if isinstance(e, TimeoutException):
                    error_message = f"Timeout in {func.__name__} during {context}."
                else:
                    error_message = f"Error in {func.__name__} ({pformat(args)}, {pformat(kwargs)}): {e} during {context}."
                
                logger.error(error_message)
                take_screenshot(driver, f"{context}_error")  # Capture screenshot for error context

                # You could consider returning None, False, or raise the exception again if you want
                # to propagate the error further in some cases
                return False  # or `None` if that is preferred for the context

        return wrapper
    return decorator

def log_args(func):
    """Decorator to log the arguments passed to a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Pretty-print the arguments for better readability
        spaces = " " * 30 
        logger.debug(f"---LOG ARGS START---\n{spaces}Calling {func.__name__} with\n{spaces}args: {pformat(args)}\n{spaces}kwargs: {pformat(kwargs)}\n{spaces}---LOG ARGS END---")
        return func(*args, **kwargs)
    return wrapper
