# -*- coding: utf-8 -*-

import os


CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

basedir = os.path.abspath(os.path.dirname(__file__))

# DB file path
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# Stores migrate data files
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_respository')

# Use get_debug_queries function
SQLALCHEMY_RECORD_QUERIES = True

# Threashold for slow loading (in seconds)
DATABASE_QUERY_TIMEOUT = 0.5

OPENID_PROVIDERS = [
	{ 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }
    ]

GMAIL_PSSWORD = os.environ.get('GMAIL_PSSWORD')

# Mail server settings
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USERNAME = 'learn.flask'
MAIL_PASSWORD = GMAIL_PSSWORD

# Administrator list
ADMINS = ['learn.flask@gmail.com']

# Open source full text seach engine
WHOOSH_BASE = os.path.join(basedir, 'search.db')

# Pagination
POSTS_PER_PAGE = 3

MAX_SEARCH_RESULTS = 50

# Available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Espanol'
}

# MS translation service
MS_TRANSLATOR_CLIENT_ID = os.environ.get('MS_ID')
MS_TRANSLATOR_CLIENT_SECRET = os.environ.get('MS_SECRET')
