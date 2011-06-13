# Django settings for blogsite project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

import logging
logging.basicConfig()

from dotcloud_serviceconfig import config

rabbitmq = config.rabbitmq
mysql = config.mysql
amqp_broker = rabbitmq.ports.amqp
mysql_server = mysql.ports.mysql

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'blogsite'
DATABASE_USER = mysql_server.username
DATABASE_PASSWORD = mysql_server.password
DATABASE_HOST = mysql_server.hostname
DATABASE_PORT = mysql_server.port

TIME_ZONE = 'UTC'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/dotcloud/current/static'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin_media/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'blogsite.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/home/dotcloud/code/bee/bee/templates',
)

BROKER_HOST = amqp_broker.hostname
BROKER_PORT = amqp_broker.port
BROKER_USER = amqp_broker.username
BROKER_PASSWORD = amqp_broker.password
CELERY_RESULT_BACKEND = "amqp"

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'djcelery',
    'south',
    'bee',
)

import djcelery
djcelery.setup_loader()

try:
    from local_settings import *
except ImportError:
    raise Exception("Create a local_settings.py file in the same dir as %s", __file__)

