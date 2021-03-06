"""
Django settings for cat project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

with open('secretkey.txt') as s:
    SECRET_KEY = s.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'userinfo',
    'pet',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cat.urls'

WSGI_APPLICATION = 'cat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

with open('dbpass.txt') as p:
    DB_PASS = p.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdb',
	'USER': 'root',
	'PASSWORD': DB_PASS,
	
    }
}

# Template

TEMPLATE_DIRS = (
	'/home/branev/Projects/cat/templates',

)

TEMPLATES = [{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': ['/home/Projects/cat/templates'],
		'APP_DIRS': False,
		'OPTIONS': {
			'context_processors': [
				"django.contrib.auth.context_processors.auth",
				"django.template.context_processors.debug",
				"django.template.context_processors.i18n",
				"django.template.context_processors.media",
				"django.template.context_processors.static",
				"django.template.context_processors.tz",
				"django.contrib.messages.context_processors.messages"
			]
		}
	}]

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = '/home/branev/Projects/cat/static/'

STATICFILES_DIRS = [
	
	("css", "/home/branev/Projects/cat/templates/css/"),
	("images", "/home/branev/Projects/cat/templates/images/"),
]


STATIC_URL = '/static/'

MEDIA_ROOT = '/home/branev/Projects/cat/media/'
