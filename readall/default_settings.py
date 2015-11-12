import os

# Flask
DEBUG = True
PROPAGATE_EXCEPTIONS = True
HOST_NAME = os.environ.get('OPENSHIFT_APP_DNS','localhost')
APP_NAME = os.environ.get('OPENSHIFT_APP_NAME','flask')
IP = os.environ.get('OPENSHIFT_PYTHON_IP','127.0.0.1')
PORT = int(os.environ.get('OPENSHIFT_PYTHON_PORT',8080))
SECRET_KEY = 'replace-with-a-random-string'

# Twitter
TWITTER_CONSUMER_KEY = 'add-values-here'
TWITTER_CONSUMER_SECRET = 'add-values-here'
TWITTER_ACCESS_TOKEN = 'add-values-here'
TWITTER_ACCESS_TOKEN_SECRET = 'add-values-here'

# Readability Parser API Keys
READABILITY_CONSUMER_KEY = 'add-values-here'
READABILITY_CONSUMER_SECRET = 'add-values-here'
READABILITY_TOKEN_KEY = 'add-values-here'
READABILITY_TOKEN_SECRET = 'add-values-here'

# Flask-Mail
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
MAIL_DEFAULT_SENDER = 'noreply@localhost'
SERVER_EMAIL = 'noreply@localhost'
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 25
EMAIL_USE_SSL = False
EMAIL_USE_TLS = False
EMAIL_TIMEOUT = 30
