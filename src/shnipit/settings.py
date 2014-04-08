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
ALLOWED_HOSTS = ["127.0.0.1", "snippet.twey.co.uk"]


# Application definition

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "account",
    "profiles",
    "bootstrapform",
    "pinax_theme_bootstrap",
    "taggit",
    "pipeline",
    "snippets",
)

TEMPLATE_DIRS = (os.path.join(BASE_DIR, "shnipit", "templates"),)

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               "django.core.context_processors.tz",
                               "django.core.context_processors.request",
                               "django.contrib.messages.context_processors.messages",
                               "account.context_processors.account",
                               "pinax_theme_bootstrap.context_processors.theme")

# Werkzeug doesn"t werk zeug good on Python 3.2.
if DEBUG and sys.version_info > (3, 2): INSTALLED_APPS += ("django_extensions",)

MIDDLEWARE_CLASSES = ("django.contrib.sessions.middleware.SessionMiddleware",
                      "django.middleware.common.CommonMiddleware",
                      "django.middleware.csrf.CsrfViewMiddleware",
                      "django.contrib.auth.middleware.AuthenticationMiddleware",
                      "django.contrib.messages.middleware.MessageMiddleware",
                      "django.middleware.clickjacking.XFrameOptionsMiddleware",
                      "account.middleware.LocaleMiddleware",
                      "account.middleware.TimezoneMiddleware")

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
STATIC_ROOT = os.path.join(BASE_DIR, "..", "static")

MEDIA_ROOT = os.path.join(STATIC_ROOT, "media")
MEDIA_URL = "/static/media/"


# snippets settings
SNIPPET_LANGUAGES = (("php", "PHP"), )
