LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'verbose',
            'filename': 'logs.log',
            'when': 'D',
            'interval': 1,
            'backupCount': 30
        },
    },
    'loggers': {
        'sqlalchemy.engine': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'sqlalchemy.dialects': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'sqlalchemy.pool': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'sqlalchemy.orm': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': "postgresql+psycopg2",
        'NAME': "test",
        'USER': 'scott',
        'PASSWORD': 'tiger',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

USE_TZ = True
TIME_ZONE = 'Asia/Taipei'