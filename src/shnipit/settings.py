"""
Django settings for shnipit project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

import sys

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Note to self: change this before going into production.
SECRET_KEY = "sdu8tc90f=tcpb0jvhyh@j019=(0h(ljmlmlpt#cp)f9t(jp9z"

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "pipeline",
    "snippets",
)

# Werkzeug doesn"t werk zeug good on Python 3.2.
if DEBUG and sys.version_info > (3, 2): INSTALLED_APPS += ("django_extensions",)

MIDDLEWARE_CLASSES = ("django.contrib.sessions.middleware.SessionMiddleware",
                      "django.middleware.common.CommonMiddleware",
                      "django.middleware.csrf.CsrfViewMiddleware",
                      "django.contrib.auth.middleware.AuthenticationMiddleware",
                      "django.contrib.messages.middleware.MessageMiddleware",
                      "django.middleware.clickjacking.XFrameOptionsMiddleware",)

ROOT_URLCONF = "shnipit.urls"

WSGI_APPLICATION = "shnipit.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "snippet",
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = "en-gb"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = "/static/"
