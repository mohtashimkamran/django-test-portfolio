"""
Django settings for portfolio project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pm_*45%x5!=3qg-gsf5iii5@d7nyt)ja-ir@u9(14sfb*3o53e'

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
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'templates')
        ],
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

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

#Application Specific data

DATA = {
    'NAME' : "MOHTAHSIM KAMRAN",
    'intro' : 'Web Developer ,Competitive programmer',
    'ABOUT_ME' : 'I am Mohtashim from New Delhi, India. I am a Data Science enthusiast,a Django Developer , a Front-end Designer, and a Competitive programmer . I am pursuing my B. Tech. in Information Technology Currently I am putting all my efforts in Machine Learning and Data structures and Algorithms . I am mostly active on Codechef, Codeforces and Leetcode at @mohtashim_mk .',
    'PROJECT' : [
        ("Dr.BoT","Made an automated AI Chat-Bot that helps users in getting first hour medical advices/needs for SMART INDIA HACKATHON. It scraps medical information from top websites and stores it in Database and provides desired information to users. Deployed on telegram and other top messengers.Technology used – Python, Python-Bot module, Selenium, Requests, Beautiful-Soup,"),
        ("Face Recognition Application","It’s a Deep Learning Module that detects faces of particular person from video/input streams. It collects face data of users and stores it in database and recognizes users from input streams.Technology used – Python, Numpy, Open Computer Vision, Image Classifiers in Database. Another module reads data from database and gives it to users. Technology used – Python, Requests, Selenium, Beautiful-Soup, SQL in Database. Another module reads data from database and gives it to users. Technology used – Python, Requests, Selenium, Beautiful-Soup, SQL"),
        ("Newsify" , "It’s an automated GUI application that gives top news on a particular topic on the basis of inputs from users. I automated the module to scrap news from top news providing websites. Cleaned and processed the data and stored it in Database. Another module reads data from database and gives it to users Technology used – Python, Requests, Selenium, Beautiful-Soup, SQL"),
    ],
    'LANGUAGES' : [
        'Python',
        'java',
        'C',
        'JavaScript',
    ]
}