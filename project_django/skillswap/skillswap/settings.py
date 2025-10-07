"""
Django settings for skillswap project.
"""

import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

# ---- Paths / dotenv (local only) ----
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")  # ignored on Azure; App Settings provide env vars

# ---- Core env-driven config ----
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "dev-only-unsafe")
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

# Azure provides this in production; fallback for local dev
AZURE_HOST = os.environ.get("WEBSITE_HOSTNAME")
ALLOWED_HOSTS = [AZURE_HOST] if AZURE_HOST else ["localhost", "127.0.0.1"]

# Trust Azure's HTTPS header and secure cookies only in prod
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

# CSRF must include your Azure hostname when deployed
CSRF_TRUSTED_ORIGINS = [f"https://{AZURE_HOST}"] if AZURE_HOST else []

# ---- Apps ----
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "widget_tweaks",
    "user_auth",
    "skill",
    "contact",
    "search",
    "review",
]

# ---- Middleware (WhiteNoise right after Security) ----
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "skillswap.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "skillswap.wsgi.application"

# ---- Database (Postgres via DATABASE_URL in Azure; SQLite locally) ----
DATABASES = {
    "default": dj_database_url.parse(
        os.environ.get("DATABASE_URL", f"sqlite:///{BASE_DIR/'db.sqlite3'}"),
        conn_max_age=600,
        ssl_require=False,  # set True if your PG provider requires SSL
    )
}

# ---- Password hashers  ----
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    # Enable next ones only if the packages are installed:
    "django.contrib.auth.hashers.Argon2PasswordHasher",        # requires argon2-cffi
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",  # requires bcrypt
]

# ---- Auth validators ----
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", "OPTIONS": {"min_length": 9}},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ---- i18n / tz ----
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ---- Static / media (WhiteNoise) ----
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ---- Auth redirects ----
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "profile_edit"
LOGOUT_REDIRECT_URL = "login"

# ---- Logging to Azure Log Stream ----
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "INFO"},
}

# ---- Default PK ----
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
