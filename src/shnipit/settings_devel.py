# Override settings for development here.

from .settings import *

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

import sys
if DEBUG and sys.version_info > (3, 2): INSTALLED_APPS += ('django_extensions',)

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.sqlite3',
        'NAME' : os.path.join(BASE_DIR, 'development.sqlite3'),
    },
}
