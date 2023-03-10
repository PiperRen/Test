# LTurner: Setting up the heroku file for deployment  3.5.23
# Trying to find differences

import os

import dj_database_url

from .settings import *

DATABASES = {
    "default": dj_database_url.config(
        default="sqlite://" + os.path.join(BASE_DIR, "db.sqlite3")
    )
}

DEBUG = False
TEMPLATE_DEBUG = False
STATIC_ROOT = os.path.join(BASE_DIR, "static")
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = ["*"]

MIDDLEWARE = (
    "whitenoise.middleware.WhiteNoiseMiddleware",
    *MIDDLEWARE,
)
