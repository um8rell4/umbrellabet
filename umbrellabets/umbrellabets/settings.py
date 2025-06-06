"""
Django settings for umbrellabets project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import environ
from decouple import config

# Инициализация environ
env = environ.Env(
    DEBUG=(bool, False)
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Чтение .env файла
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'ads',
    'bets',
    'core',
    'events',
    'matches',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'accounts.middleware.EmailConfirmationMiddleware',
]

ROOT_URLCONF = 'umbrellabets.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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

WSGI_APPLICATION = 'umbrellabets.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}


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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'accounts:profile'
LOGOUT_REDIRECT_URL = 'accounts:login'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Настройки email для восстановления пароля
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Для production используйте SMTP
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')  # Ваш email для отправки
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')  # Пароль от email
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # Email отправителя
SERVER_EMAIL = EMAIL_HOST_USER

# Настройки сайта для писем
SITE_NAME = "UmbrellaBets"  # Будет использоваться в письмах

# Важно для Yandex
EMAIL_TIMEOUT = 10  # Таймаут соединения

EMAIL_USE_TLS = False  # Используйте либо SSL, либо TLS
DEFAULT_CHARSET = 'utf-8'

PANDASCORE_API_KEY = config('PANDASCORE_API_KEY')

# Настройки для ставок
BET_SETTINGS = {
    'MIN_BET_AMOUNT': 10.00,
    'MAX_BET_AMOUNT': 100000.00,
    'DEFAULT_ODDS_UPDATE_INTERVAL': 5,  # секунды
}

# Настройки Jazzmin админки
JAZZMIN_SETTINGS = {
    "site_title": "UmbrellaBet Admin",
    "site_header": "UmbrellaBet",
    "site_brand": "UmbrellaBet",
    "site_logo": None,
    "login_logo": None,
    "welcome_sign": "Добро пожаловать в админ-панель CyberBet",
    "copyright": "CyberBet Ltd",
    "search_model": ["auth.User", "accounts.UserProfile"],

    # Цветовая схема
    "theme": "darkly",  # или "flatly", "minty", "litera"

    # Иконки для приложений
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "accounts.UserProfile": "fas fa-user-circle",
        "accounts.Transaction": "fas fa-money-bill-wave",
    },

    # Меню
    "topmenu_links": [
        {"name": "Главная", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Сайт", "url": "/", "new_window": True},
    ],

    # Боковое меню
    "usermenu_links": [
        {"name": "Сайт", "url": "/", "new_window": True},
        {"model": "auth.user"}
    ],

    # Показать/скрыть приложения
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],

    # Кастомные ссылки
    "custom_links": {
        "accounts": [{
            "name": "Статистика пользователей",
            "url": "admin:accounts_userprofile_changelist",
            "icon": "fas fa-chart-bar",
            "permissions": ["accounts.view_userprofile"]
        }]
    },
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-primary",
    "accent": "accent-primary",
    "navbar": "navbar-primary navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "darkly",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}

# Бэкенды аутентификации
AUTHENTICATION_BACKENDS = [
    'accounts.backends.EmailOrUsernameModelBackend',  # Наш кастомный бэкенд
    'django.contrib.auth.backends.ModelBackend',      # Стандартный бэкенд (запасной)
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'accounts': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}
