from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'AppVac',
        'USER': 'postgres',
        'PASSWORD': 'admin247',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}