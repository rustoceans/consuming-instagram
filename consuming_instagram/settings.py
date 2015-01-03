# coding: utf-8
"""
Django settings for consuming_instagram project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.request',)

import sys
from decouple import config
from dj_database_url import parse as db_url
from unipath import Path
BASE_DIR = Path(__file__).parent


# Templates

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

TEMPLATE_DEBUG = DEBUG

TESTING = 'test' in sys.argv

ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '.herokuapp.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'devserver',
    'south',
    'consuming_instagram.core',
)

INSTALLED_APPS += (
    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'consuming_instagram.urls'

WSGI_APPLICATION = 'consuming_instagram.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///' + BASE_DIR.child('db.sqlite3'),
        cast=db_url),
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = BASE_DIR.child('staticfiles')
STATIC_URL = '/static/'

TEMPLATE_DIRS = BASE_DIR.child('core', 'templates')

# Cache
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

CACHE_ACTIVE = config('CACHE_ACTIVE', default=False, cast=bool)

if CACHE_ACTIVE:
    CACHES = {
        'default': {
                'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
                'BINARY': True,
                'LOCATION': config('CACHE_LOCATION'),
                'OPTIONS': {
                    'ketama': True,
                    'tcp_nodelay': True,
                },
                'TIMEOUT': config('CACHE_TIMEOUT', default=500, cast=int),
            },
    }
else:  # Assume development mode
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }


TEMPLATE_STRING_IF_INVALID = 'CONTEXT_ERROR'


# Logging
def skip_on_testing(record):
    return not TESTING


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'normal': {
            'format': '%(levelname)s %(name)s %(message)s'
        },
    },
    'filters': {
     'require_debug_true': {
         '()': 'django.utils.log.RequireDebugTrue',
         },
     'skip_on_testing': {
        '()': 'django.utils.log.CallbackFilter',
        'callback': skip_on_testing,
        },
    },
    'handlers': {
        'stderr': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'normal',
            'filters': ['skip_on_testing'],
        },
    },
    'loggers': {
        'consuming_instagram': {
            'handlers': ['stderr'],
            'level': 'INFO',
        },
    },
}
