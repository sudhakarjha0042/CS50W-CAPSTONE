from pathlib import Path
import os

BASE_DIRS = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-0%a#awa#c)+_izo2j@7z!djh4erk+gk3@b##gk3wxacz4@@w^+'

DEBUG = True

<<<<<<< HEAD
ALLOWED_HOSTS = ['192.168.0.104','127.0.0.1']

=======
ALLOWED_HOSTS = ['192.168.0.104','127.0.0.1','astoundingly-underground-proton-den-dev.wayscript.cloud','quietly-discrete-force-chateau-dev.wayscript.cloud','absolutely-discrete-tyrannosaurus-hamlet-dev.wayscript.cloud']

# Application definition
>>>>>>> origin/web50/projects/2020/x/capstone

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'NewsJunction',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'CS50W_Final.urls'

AUTHENTICATION_BACKENDS = [    'django.contrib.auth.backends.ModelBackend',    'allauth.account.auth_backends.AuthenticationBackend',]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIRS / "NewsJunction/templates/NewsJunction"],
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

WSGI_APPLICATION = 'CS50W_Final.wsgi.application'


<<<<<<< HEAD
=======
# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
>>>>>>> origin/web50/projects/2020/x/capstone

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIRS / 'db.sqlite3',
    }
}

STATICFILES_DIRS = [
    BASE_DIRS / "NewsJunction/static",
]

MEDIA_ROOT = os.path.join(BASE_DIRS, 'media')
MEDIA_URL = '/media/'

<<<<<<< HEAD

=======
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
>>>>>>> origin/web50/projects/2020/x/capstone

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


<<<<<<< HEAD
=======
# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

>>>>>>> origin/web50/projects/2020/x/capstone
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


<<<<<<< HEAD
STATIC_URL = '/static/'

=======
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
>>>>>>> origin/web50/projects/2020/x/capstone

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 2

<<<<<<< HEAD
=======
# settings.py
>>>>>>> origin/web50/projects/2020/x/capstone
LOGIN_URL = '/accounts/login/'

LOGIN_REDIRECT_URL = '/'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email'
        ],
        'AUTH_PARAMS': {
            'access_type': 'online'
        }
    }
}

ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
<<<<<<< HEAD
=======

CORS_ORIGIN_WHITELIST = ["https://astoundingly-underground-proton-den-dev.wayscript.cloud","https://absolutely-discrete-tyrannosaurus-hamlet-dev.wayscript.cloud"]
CSRF_TRUSTED_ORIGINS = ["https://astoundingly-underground-proton-den-dev.wayscript.cloud","https://absolutely-discrete-tyrannosaurus-hamlet-dev.wayscript.cloud"]
>>>>>>> origin/web50/projects/2020/x/capstone
