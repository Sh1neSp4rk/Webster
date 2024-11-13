# sites/SITE_TEMPLATE/credentials.py

# This file contains sensitive data such as usernames and passwords.
# It is best practice to store these in environment variables or an encrypted configuration.

# Example format (NOTE: Do not store sensitive data in plain text in production!)

credentials = {
    'login': {
        'username': 'your_username',  # Replace with your actual username or fetch from environment variables
        'password': 'your_password'   # Replace with your actual password or fetch from environment variables
    },
    'dashboard': {
        'admin_username': 'admin',
        'admin_password': 'admin_password_here'
    }
}

# Usage:
# In your actions.py, you can import the credentials dictionary:
# from sites.SITE_TEMPLATE.credentials import CREDENTIALS
# Then use CREDENTIALS['login']['username'] to get the username for login
