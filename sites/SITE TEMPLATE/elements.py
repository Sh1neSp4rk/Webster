# sites/SITE_TEMPLATE/elements.py

# This file contains the selectors and paths for different page elements.
# The elements are grouped by page, and each page has its own section with URL and element definitions.

# Login page elements
login_elements = {
    'url': 'login',  # Reference to the URL in urls.py
    'username': 'input[name="username"]',  # The selector for the username input field
    'password': 'input[name="password"]',  # The selector for the password input field
    'login_button': 'button[type="submit"]',  # The selector for the login button
    'error_message': '.error-message'  # An optional selector for error messages (e.g., incorrect login)
}

# Dashboard page elements
dashboard_elements = {
    'url': 'dashboard',  # Reference to the URL in urls.py
    'entry_count': '#entryCount',  # Selector for the entry count element on the dashboard
    'menu_button': '#menuButton',  # Selector for the menu button on the dashboard
}

# Example of page-specific elements: Inspections page
inspections_elements = {
    'url': 'inspections',  # Reference to the URL in urls.py
    'entry_count': '#entryCount',  # Example element for entry count
    'export_buttons': {
        'first': '.export-btn-first',  # Selector for first export button
        'summary': {
            'second': '#btnSummaryExport',  # Selector for summary export button
            'selection': '#createSummaryExcel'  # Selector for selecting the export option
        }
    },
    'date_filter': {
        'start_date': '#startDate',  # Selector for the start date input
        'end_date': '#endDate',  # Selector for the end date input
    }
}