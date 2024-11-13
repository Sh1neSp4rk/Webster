# sites/SITE_TEMPLATE/actions.py

# This file contains all the functions that interact with the page elements
# Each function should use the defined selectors and paths in elements.py to perform actions like click, write, etc.

from framework.actions import click, write, find  # Import actions from the framework

def login(driver, username, password):
    """
    Perform login action using the provided username and password.
    :param driver: Selenium WebDriver instance
    :param username: Username to login
    :param password: Password to login
    :return: True if login is successful, False otherwise
    """
    if not (find('login_elements', 'username') and
            write('login_elements', 'username', username) and
            find('login_elements', 'password') and
            write('login_elements', 'password', password) and
            click('login_elements', 'login_button')):
        return False
    return True

def navigate_to_dashboard(driver):
    """
    Navigate to the dashboard page using the URL from urls.py.
    :param driver: Selenium WebDriver instance
    :return: True if navigation is successful, False otherwise
    """
    if not find('dashboard_elements', 'url'):
        return False
    return True

def export_inspections_report(driver):
    """
    Click the 'export' buttons for inspections and download the report.
    :param driver: Selenium WebDriver instance
    :return: None
    """
    click('inspections_elements', 'export_buttons.first')  # Click on the first export button
    click('inspections_elements', 'export_buttons.summary.selection')  # Select the summary export
