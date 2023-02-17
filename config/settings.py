from .base import *

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'www.petpls.ca',
                 'petpls.ca']

INSTALLED_APPS += ['storages']

AWS_PRELOAD_METADATA = True
AWS_ACCESS_KEY_ID = config_secret['S3']['key']
AWS_SECRET_ACCESS_KEY = config_secret['S3']['secret']
AWS_STORAGE_BUCKET_NAME = config_secret['S3']['bucket_name']
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
STATICFILES_STORAGE = 'config.custom_storages.StaticStorage'

# DEFAULT_FILE_STORAGE = 'config.custom_storages.UploadStorage'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config_secret['DB']['name'],
        'USER': config_secret['DB']['user'],
        'PASSWORD': config_secret['DB']['password'],
        'HOST': config_secret['DB']['host'],
        'PORT': '5432',
    }
}

