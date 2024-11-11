import environ
import os
from pathlib import Path
from django.urls import reverse_lazy
from dotenv import load_dotenv
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Apartado configuración con variables de entorno
env = environ.Env()

# Define el archivo .env y lee las variables de entorno
env_file = os.path.join(os.path.dirname(BASE_DIR), ".env")
env.read_env(env_file=env_file, overwrite=True)

# Configuración del secreto y entorno de desarrollo
SECRET_KEY_DEFAULT = 'django-insecure-ixnzv*k#2j8g6@y&iq!bjg_l188nh0b-y@v8vg(mv8hqx@+@uv'
SECRET_KEY = env("SECRET_KEY", default=SECRET_KEY_DEFAULT)

DEBUG = env.bool('DJANGO_DEBUG', default=True)

ENVIRONMENT_RUN = env("ENVIRONMENT_RUN", default="local")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=['*'])

# Fin apartado entorno

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.usuarios',
    'apps.pacientes',
    'apps.vacunas'
]

AUTH_USER_MODEL = 'usuarios.Usuario'

LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('inicio')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Base de datos
load_dotenv()  # Carga las variables de entorno desde el archivo .env

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'AppVac_ECOM'),
        'USER': os.getenv('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'contraseña'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("POSTGRES_DB"),
        'USER': env("POSTGRES_USER"),
        'PASSWORD': env("POSTGRES_PASSWORD"),
        'HOST': env("POSTGRES_HOST"),
        'PORT': env("POSTGRES_PORT"),
    }
}'''

# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internacionalización
LANGUAGE_CODE = 'es-Ar'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Contenido Media
RUTA_CARPETA_MEDIA = os.path.join(BASE_DIR, "media")
MEDIA_URL = "media/"
MEDIA_ROOT = RUTA_CARPETA_MEDIA

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'