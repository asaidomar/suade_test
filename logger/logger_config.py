import os
LEVEL = os.environ.get("LOG_LEVEL", "DEBUG")


CONFIG = {
    'loggers': {
        'main': {
            'level': LEVEL,
            'propogate': True,
            'handlers': ['console']
        },
        'django.db.backends': {
            'level': 'ERROR',
        },
    },
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'console': {
            'formatter': 'default', 'class': 'logging.StreamHandler',
            'level': LEVEL
        }
    },
    'root': {
        'level': LEVEL,
        'propogate': True,
        'handlers': ['console']
    },
    'formatters': {
        'default': {
            'format': '%(asctime)s|%(levelname)s|%(name)'
                      's(%(funcName)s:%(lineno)s)|%(message)s'
        }
    }

}
