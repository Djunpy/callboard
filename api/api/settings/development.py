import socket
import os
from .base import *


SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    "http://127.0.0.1:3000",
]


#===========DEBUG_TOOLBAR===============
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())

INTERNAL_IPS = [
    ip[: ip.rfind(".")
] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

INSTALLED_APPS.append("debug_toolbar")
MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
#===========================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT')
#     }
# }

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = env('EMAIL_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'