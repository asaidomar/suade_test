# noqa
from .base import *

DATABASES = {
    'default': env.db('TEST_DATABASE_URL',
                      default='sqlite:////{}/db.testing.sqlite3'.format(
                          BASE_DIR.path('db'))),
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
    }
}