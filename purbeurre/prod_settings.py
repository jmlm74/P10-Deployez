import os

from .settings import *


# debug
DEBUG = False
TEMPLATE_DEBUG = False

# disable django debug toolbar
INTERNAL_IPS = []

# security
ALLOWED_HOSTS = ['*', ]
SECRET_KEY = get_env_variable('SECRET_KEY', '')

# postgres database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'purbeurre',
        'USER': 'jmlm',
        'PASSWORD': 'jmlmpw',
        'HOST': '192.168.1.99',
        'PORT': '5432',
    }
}
WSGI_APPLICATION = 'purbeurre.wsgi.application'

# static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# white noise for static files
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
