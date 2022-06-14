from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'todo',
        'USER': 'A1eksAwP',
        'PASSWORD': 'adminadmin',
        'HOST': 'db',
        'PORT': '5432'
    }
}