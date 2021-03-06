import os
from pathlib import Path
from django.conf.locale.en import formats as es_formats
from django.conf import settings

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # take environment variables from .env.

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['pdf-generat.herokuapp.com', '127.0.0.1']
ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'questionnaire',

    'crispy_forms',
    'wkhtmltopdf',
    'nested_admin',
    'bootstrapform',
]

# !
from pathlib import Path
CSV_DIRECTORY = Path("media/")
TEX_DIRECTORY = Path("media/")
# !

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS':True,
        'OPTIONS':{
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = '/static/'


if os.getenv('RUN_IN_DOCKER') == 'False':
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
else:
    STATIC_ROOT = '/var/www/pdf_generator/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static'),
    ]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# CRISPY_TEMPLATE_PACK = 'bootstrap4'
WKHTMLTOPDF_CMD = '/usr/bin/wkhtmltopdf'


SE_L10N = False
es_formats.DATETIME_FORMAT = 'd. m. yy'

ROOT = os.path.dirname(os.path.abspath(__file__))
USER_DID_NOT_ANSWER = getattr(settings, "USER_DID_NOT_ANSWER", "Left blank")
TEX_CONFIGURATION_FILE = getattr(settings, "TEX_CONFIGURATION_FILE", Path(ROOT, "doc", "example_conf.yaml"))
SURVEY_DEFAULT_PIE_COLOR = getattr(settings, "SURVEY_DEFAULT_PIE_COLOR", "red!50")
CHOICES_SEPARATOR = getattr(settings, "CHOICES_SEPARATOR", ",")
EXCEL_COMPATIBLE_CSV = False
DEFAULT_SURVEY_PUBLISHING_DURATION = 7

# email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_RECIPIENT = os.getenv('EMAIL_HOST_RECIPIENT')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

# celery
CELERY_NUM_WORKERS = 2
if os.getenv('RUN_IN_DOCKER') == 'False':
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
    CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
else:
    CELERY_BROKER_URL = "redis://redis:6379"
    CELERY_RESULT_BACKEND = "redis://redis:6379"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"

