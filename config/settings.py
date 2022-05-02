"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os, json
import secrets
# from django.core.exceptions import ImproperConfigured
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
secret_file = os.path.join(BASE_DIR,'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    return secrets[setting]
    

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'main',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'bootstrap4',
    'gallery',
    'photoguide',
    'collection',
    'storages',
    'rest_framework',
]


# AWS_ACCESS_KEY_ID = 'Access key ID 입력' # .csv 파일에 있는 내용을 입력 Access key ID
# AWS_SECRET_ACCESS_KEY = 'Secret acess Key 입력' # .csv 파일에 있는 내용을 입력 Secret access key
# AWS_REGION = 'ap-northeast-2'

# ###S3 Storages
# AWS_STORAGE_BUCKET_NAME = 'lee-teset-bucket' # 설정한 버킷 이름
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME,AWS_REGION)
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'path/to/store/my/files/')




AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]
SITE_ID = 1
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'




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
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 's3',
        # 'NAME': 'DB',
        'USER': 'admin',
        'PASSWORD': get_secret("PASSWORD"),
        'HOST': get_secret("DATABASE"),
        'PORT': 3306
        }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "main.validators.CustomPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# STATIC_URL = os.path.join(BASE_DIR,'static')

AUTH_USER_MODEL ='main.User'
ACCOUNT_SIGNUP_REDIRECT_URL = 'index'
LOGIN_REDIRECT_URL ='/'


ACCOUNT_AUTHENTICATION_METHOD = 'email' #로그인시 유저네임이 아니라 이메일로 만들기
ACCOUNT_EMAIL_REQUIRED = True #회원가입시 필수 이메일을 필수항목으로 만들기
ACCOUNT_USERNAME_REQUIRED = False #유저네임을 필수항목에서 제거
ACCOUNT_SIGNUP_FORM_CLASS ='main.forms.SignupForm'
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "account_email_confirmation_done"
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "account_email_confirmation_done"

ACCOUNT_SESSION_REMEMBER = True # 브라우저를 닫아도 세션기록 유지(로그인이 안풀림)
SESSION_COOKIE_AGE = 3600 # 쿠키를 한시간 저장(세션)

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'syg3793@gmail.com'
EMAIL_HOST_PASSWORD ='canu6858!@'
EMAIL_USE_TLS =True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
MAIN_URL = 'http://127.0.0.1:8000/'
STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    # os.path.join(BASE_DIR, 'main', 'static'),
    os.path.join(BASE_DIR, 'static'),
) 

# 이걸 추가해야 django네 메세지 나오게 함
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

# s3 연결
AWS_ACCESS_KEY_ID = get_secret("ACCESS_KEY") # .csv 파일에 있는 내용을 입력 Access key ID
AWS_SECRET_ACCESS_KEY = get_secret("ACCESS_SECRET_KEY") # .csv 파일에 있는 내용을 입력 Secret access key
AWS_REGION = 'ap-northeast-2'

###S3 Storages
AWS_STORAGE_BUCKET_NAME = 'photomarble' # 설정한 버킷 이름
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME,AWS_REGION)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')