# Django settings for <your project>
import socket
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '.')).replace('\\', '/')

if socket.gethostname() == 'your-production-hostname':
    environ = 'production'
else:
    environ = 'development'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = DEBUG

ADMINS = (
     ('your name', 'your-email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {
            'autocommit': True,
        },
    },
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True


# ------------------------- #
# Media                     #
# ------------------------- #
MEDIA_ROOT = os.path.join(PROJECT_ROOT, '../public/media')
STATIC_ROOT = os.path.join(PROJECT_ROOT, '../public/static')
STATICFILES_ROOT = os.path.join(PROJECT_ROOT, '../public/static-media') # actual location of our static files

MEDIA_URL = '/media/'
STATIC_URL = '/static-media/' if DEBUG else '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'grappelli/'


# ------------------------- #
# Staticfiles & storage     #
# ------------------------- #
STATICFILES_DIRS = (
    STATICFILES_ROOT,
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (

    # Enable if using johnny-cache
#    'johnny.middleware.LocalStoreClearMiddleware',
#    'johnny.middleware.QueryCacheMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'library.context_processors.settings',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, '../templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'south',
    'debug_toolbar',
    'compressor',
    'django_extensions',
    'easy_thumbnails',
    # Mine
#    'easyedit',

    # admin
    'grappelli',
    'django.contrib.admin',
    'django.contrib.admindocs',

    # Local
    'content',


    # Optional
#    'johnny',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


# ------------------------- #
# Debug toolbar             #
# ------------------------- #
INTERNAL_IPS = ('127.0.0.1', )
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'HIDE_DJANGO_SQL': False,
    'SHOW_TOOLBAR_CALLBACK': lambda req: DEBUG, # Show whenever debugging is on
}


# ------------------------- #
# Development settings      #
# ------------------------- #
if environ == 'development':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(PROJECT_ROOT, '../dev.db'),
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        },
#        'default': {
#            'ENGINE': 'django.db.backends.postgresql_psycopg2',
#            'NAME': '',
#            'USER': '',
#            'PASSWORD': '',
#            'HOST': 'localhost',
#            'PORT': '5432',
#            'OPTIONS': {
#                'autocommit': True,
#            },
#        },
    }

