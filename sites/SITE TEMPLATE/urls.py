# sites/SITE_TEMPLATE/urls.py

# This file stores the base URLs and relative paths for different pages on the site.
# Use this file to map out the structure of the website and make URLs easier to manage.

# Base URLs for different sections of the website
urls = {
    'main': 'https://www.example.com',  # Main website URL
    'login': 'https://www.example.com/login',  # Login page URL
    'dashboard': 'https://www.example.com/dashboard',  # Dashboard URL
    'inspections': 'https://www.example.com/inspections',  # Inspections page URL
}

# Usage example:
# In elements.py, you would use the reference 'login' to access the full URL:
# url = urls['login']  # This would give you 'https://www.example.com/login'
