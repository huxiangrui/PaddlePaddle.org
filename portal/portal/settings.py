#   Copyright (c) 2018 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Django settings for portal project.

Generated by 'django-admin startproject' using Django 1.8.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import time
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'secret')

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

ENV = os.environ.get('ENV', None)

if ENV == 'production':
    DEBUG = False
else:
    DEBUG = True

DEFAULT_DOCS_VERSION = '1.0.0' if ENV in ['production', 'staging'] else 'develop'

SIDE_NAVIGATION = [
    {
        'title': {
            'en':'Documentation',
            'zh': u'\u4f7f\u7528\u6587\u6863'
        },
        'path': '/docs',
        'dir': os.environ.get('PADDLE_PATH', None)
    },
    {
        'title': {
            'en':'API',
            'zh':'API'
        },
        'path': '/api',
        'dir': os.environ.get('PADDLE_PATH', None)
    },
    {
        'title': {
            'en':'Book',
            'zh':u'\u6df1\u5ea6\u5b66\u4e60101'
        },
        'path': '/book',
        'dir': os.environ.get('BOOK_PATH', None)
    },
    {
        'title': {
            'en':'Models',
            'zh':u'\u6a21\u578b\u5e93'
        },
        'path': '/models',
        'dir': os.environ.get('MODELS_PATH', None)
    },
    {
        'title': {
            'en':'Mobile',
            'zh':u'\u79fb\u52a8\u7aef'
        },
        'path': '/mobile',
        'dir': os.environ.get('MOBILE_PATH', None)
    }
]

VISUALDL_SIDE_NAVIGATION = [
    {
        'title': {
            'en':'Documentation',
            'zh': u'\u4f7f\u7528\u6587\u6863'
        },
        'path': '/visualdl',
        'dir': os.environ.get('VISUALDL_PATH', None)
    },
]

VERSIONS = [
    { 'name': '0.10.0', 'api': 'v2' },
    { 'name': '0.11.0', 'api': 'v2' },
    { 'name': '0.12.0', 'api': 'v2' },
    { 'name': '0.13.0', 'api': 'Fluid' },
    { 'name': '0.14.0', 'api': 'Fluid' },
    { 'name': '0.15.0', 'api': 'Fluid' },
    { 'name': '1.0.0', 'api': 'Fluid'},
]

if DEBUG:
    VERSIONS.append({ 'name': 'develop_doc', 'api': 'Fluid' })
    VERSIONS.append({ 'name': 'develop', 'api': 'Fluid' })

if DEBUG:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.paddlepaddle.localhost']
else:
    ALLOWED_HOSTS = ['.paddlepaddle.org', '.ap-southeast-1.elb.amazonaws.com', '.ap-southeast-1.compute.amazonaws.com']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portal',
    'visualDL',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'portal.middleware.subdomain.SubdomainMiddleware',
)

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

PREFERRED_VERSION_NAME = 'preferred_version'
PREFERRED_API_VERSION_NAME = 'preferred_api_version'

ROOT_URLCONF = 'portal.urls'

SPHINX_CONFIG_DIR = os.path.join(BASE_DIR, 'portal/config')
WORKSPACE_DIR = 'documentation'
PAGES_DIR = '/var/pages' if ENV in ['production', 'staging'] else BASE_DIR
MENUS_DIR = os.path.join(PAGES_DIR, 'menus')
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'portal/templates'), PAGES_DIR]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'portal.context_processors.base_context',
            ],
        },
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT': 0 if DEBUG else 300
    }
}

WSGI_APPLICATION = 'portal.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en', _('English')),
    ('zh', _('Chinese')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

APPEND_SLASH = True

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'portal/static/'),
    os.path.join(BASE_DIR, 'visualDL/static/'),
)

STATIC_ROOT = 'static/'
STATIC_URL = '/static/'

TEMPORARY_DIR = '/tmp/'

SUPPORT_MENU_JSON = False

SERVER_START_TIME = time.time()
