# noqa
from .base import *

DEBUG = False

SECRET_KEY = env('SECRET_KEY')

INSTALLED_APPS = ['', ] + INSTALLED_APPS

# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DBNAME'),
        'USER': env('DBUSER'),
        'PASSWORD': env('DBPASSWORD'),
        'HOST': env('DBHOST'),
    }
}

MIDDLEWARE.insert(
    MIDDLEWARE.index('django.middleware.common.CommonMiddleware'),
    'corsheaders.middleware.CorsMiddleware'
)


# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'suade_test_cache_table',
    }
}

# CORS
CORS_ORIGIN_ALLOW_ALL = True

# Logging

LOG_LEVEL = env.str('LOG_LEVEL', default='INFO')

MEDIA_ROOT = "/srv/media"

CHECK_GOOGLE_RECAPTCHA = False
ACCOUNT_EMAIL_VERIFICATION = True

os.environ['wsgi.url_scheme'] = 'https'
