# coding: utf-8
import os
import environ


# Load operating system environment variables and then prepare to use them
env = environ.Env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY', default="MySecret")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['0.0.0.0', 'localhost', '127.0.0.0'])


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Database postgres apps
    'django.contrib.postgres',
    'django.contrib.gis',
    # 3rd part apps
    'admin_reorder',
    'django_json_widget',
    'django_admin_json_editor',
    'ckeditor',
    'django_extensions',
    'raven.contrib.django.raven_compat',
    'reversion',
    'reversion_compare',
    'import_export',
    # My apps
    'collection',
    'digitalassetsmanagement',
    'event',
    'exhibition',
    'glossary',
    'home',
    'location',
    'management',
    'person',
    'publication',
]

# Imports
from django.utils.translation import ugettext_lazy as _

MIDDLEWARE = [
    'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
    'reversion.middleware.RevisionMiddleware',
]

ROOT_URLCONF = 'guia.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'guia.wsgi.application'


### From Json Admin Widget
DATA_SCHEMA = {
    'type': 'object',
    'title': 'Data',
    'properties': {
        'text': {
            'title': _('key'),
            'type': 'string',
            'format': 'input',
        },
        'status': {
            'title': _('value'),
            'type': 'string',
            'format': 'input',
        },
    },
}

# Add reversion models to admin interface:
ADD_REVERSION_ADMIN=True


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': env.str('DB_NAME'),
        'USER': env.str('DB_USER'),
        'PASSWORD': env.str('DB_PASSWORD'),
        'HOST': env.str('DB_HOST', default='postgres'),
    }
}

IMPORT_EXPORT_USE_TRANSACTIONS = True
IMPORT_EXPORT_SKIP_ADMIN_LOG = False

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators
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


# Provide a lists of languages which your site supports.
LANGUAGES = (
    ('pt-br', _('Portuguese')),
    ('en', _('English')),
)

LANGUAGE_CODE = 'pt-br'

# Tell Django where the project's translation files should be.
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


MEDIA_URL   = '/media/'

MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

FIXTURE_DIRS = (os.path.join(BASE_DIR, 'fixtures'),)


# Ckeditor configuration
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat']
        ]
    }
}

## From Django Model Admin Reorder https://github.com/mishbahr/django-modeladmin-reorder

ADMIN_REORDER = (
    {'app': 'auth',
    'models': ('auth.User', 'auth.Group', 'home.Post')},
    {'app': 'collection',
    'label': 'Guia IMS',
    'models': ('collection.Collection',
                'exhibition.Exhibition',
                'publication.Publication',
                'event.Event',
                'person.Person',)},
    {'app': 'digitalassetsmanagement',
    'label': 'Digital Assets Management',
    'models': ('digitalassetsmanagement.Item',)},
    {'app': 'management',
    'label': 'Gestão do Acervo',
    'models': ('management.ManagementUnit',
                {'model': 'location.Location', 'label': 'Locais de Guarda'},
                'management.Acquisition',
                'management.Procedure')},
    {'app': 'glossary',
    'label': 'Glossário',
    'models': ('glossary.AggregationType',
                'glossary.AccessCondition',
                'glossary.DescriptionLevel',
                'glossary.GenreTag')},
)


# Sentry Configuration
if env('DJANGO_SENTRY_DSN', default=False):
    SENTRY_DSN = env('DJANGO_SENTRY_DSN')
    SENTRY_CLIENT = env('DJANGO_SENTRY_CLIENT', default='raven.contrib.django.raven_compat.DjangoClient')
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry', ],
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s '
                        '%(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'sentry': {
                'level': 'ERROR',
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console', ],
                'propagate': False,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console', ],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['console', ],
                'propagate': False,
            },
            'django.security.DisallowedHost': {
                'level': 'ERROR',
                'handlers': ['console', 'sentry', ],
                'propagate': False,
            },
        },
    }
