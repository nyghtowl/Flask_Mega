#_*_ coding: utf-8 _*_

import os

basedir = os.path.abspath(os.path.dirname(__file__))

GMAIL_PSSWORD = os.environ.get('GMAIL_PSSWORD')

# DB file path
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# Stores migrate data files
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_respository')

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
	{ 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }
    ]

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
    'en': 'English'
    'es': 'Espanol'
}