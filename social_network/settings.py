"""
Django settings for social_network project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from configs.variable_system import *
from celery.schedules import crontab

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e76#g*9-w+$i9hn@*r+xy^^@253fp*@+ahs2ebhpwu$5_x^x(g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_celery_beat',
    # 'corsheaders',
    'api_app',
    # 'django_celery_results',
    'celery'
    # 'django_crontab',
    # 'anymail',
]

DATE_FORMAT = '%d-%m-%Y'

DATETIME_FORMAT = '%d-%m-%Y %H:%M:%S'

DATE_INPUT_FORMATS = [
    '%d/%m/%Y',
    '%Y-%m-%d',
    '%d-%m-%Y',
    '%Y/%m/%d'
]

DATETIME_INPUT_FORMATS = [
    '%Y-%m-%d %H:%M:%S',
    '%Y/%m/%d %H:%M:%S',
    '%d-%m-%Y %H:%M:%S',
    '%d/%m/%Y %H:%M:%S'
]

REST_FRAMEWORK = {
    'DATE_FORMAT': DATE_FORMAT,
    'DATETIME_FORMAT': DATETIME_FORMAT,
    'DATE_INPUT_FORMATS': DATE_INPUT_FORMATS,
    'DATETIME_INPUT_FORMATS': DATETIME_INPUT_FORMATS,
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FormParser'
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'api_app.throttling.UserThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '1/second',
    },
    'EXCEPTION_HANDLER': 'api_app.throttling.custom_exception_handler'
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'middleware.auth_user_middleware.AuthUserMiddleware',
]

# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
# ]

ROOT_URLCONF = 'api_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'social_network.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'social_network', #'mypt',
        'USER': 'admin', #'root',
        'PASSWORD': '123456', #'0000',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1'
    },
    'redis_db0': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/0'
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_BROKER_URL = CACHES['redis_db0']['LOCATION'] #'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = CACHES['redis_db0']['LOCATION'] #'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
# CELERY_TASK_ROUTES = {
#     'api_app.tasks.create_blog': {'queue': 'alobolobola'},
#     'api_app.tasks.*': {'queue': 'alobolobola'},
# }
# CELERY_TASK_ANNOTATIONS = {
#     '*': {
#         'max_retries': 3
#     }
# }

# CELERY_BEAT_SCHEDULE = {
#     'Task_one_schedule': {
#         'task': 'api_app.tasks.add',
#         'schedule': crontab(hour=10, minute=0),
#         'args': (16, 16)
#     },
# }

CRONJOBS = [
    (CRON_JOB['scheduled_job_send_mail'], CRON_JOB['cron_app'] + '.' + CRON_JOB['cron_module'] + '.' + CRON_JOB['job_send_mail']['send_mail']),
    (CRON_JOB['scheduled_job_send_mail'], CRON_JOB['cron_app'] + '.' + CRON_JOB['cron_module'] + '.' + CRON_JOB['job_send_mail']['email_message']),
    (CRON_JOB['scheduled_job_send_mail'], 'api_app.cron_jobs.multi_mail'),
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = SMTP_EMAIL['host'] #'smtp.fpt.net'
EMAIL_PORT = SMTP_EMAIL['port'] #587
EMAIL_HOST_USER = SMTP_EMAIL['host_user'] #'phuongnam.kimnt1@fpt.net'
EMAIL_HOST_PASSWORD = SMTP_EMAIL['host_passwor'] #'K@12345abcd'
EMAIL_USE_TLS = SMTP_EMAIL['use_tls'] #True or False
EMAIL_USE_SSL = SMTP_EMAIL['use_ssl'] #True or False
