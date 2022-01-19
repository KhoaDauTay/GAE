"""
Base settings to build other settings files upon.
"""
import os
from pathlib import Path

import environ

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
# erp_greenwich/
APPS_DIR = ROOT_DIR / "erp_greenwich"
env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(ROOT_DIR / ".env"))

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)
# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "Asia/Ho_Chi_Minh"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = False
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(ROOT_DIR / "locale")]

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {"default": env.db("DATABASE_URL")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True
# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "config.urls"
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # "django.contrib.humanize", # Handy template tags
    "django.contrib.admin",
    "django.forms",
]
THIRD_PARTY_APPS = [
    "oauth2_provider",
    "crispy_forms",
    "crispy_bootstrap5",
    "allauth",
    "allauth.account",
    # "allauth.socialaccount",
    "django_celery_beat",
    "rest_framework",
    # "rest_framework.authtoken",
    "corsheaders",
]

LOCAL_APPS = [
    "erp_greenwich.users",
    "erp_greenwich.auth"
    # Your stuff: custom apps go here
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIGRATIONS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#migration-modules
MIGRATION_MODULES = {"sites": "erp_greenwich.contrib.sites.migrations"}

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "oauth2_provider.backends.OAuth2Backend",
    "django.contrib.auth.backends.ModelBackend",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "users:redirect"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "account_login"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "oauth2_provider.middleware.OAuth2TokenMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(APPS_DIR / "static")]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR / "media")
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#dirs
        "DIRS": [str(APPS_DIR / "templates")],
        # https://docs.djangoproject.com/en/dev/ref/settings/#app-dirs
        "APP_DIRS": True,
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "erp_greenwich.users.context_processors.allauth_settings",
            ],
        },
    }
]

# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (str(APPS_DIR / "fixtures"),)

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = "admin/"
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("""khoa""", "khoadautay@gmail.com")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
                      "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

# Celery
# ------------------------------------------------------------------------------
if USE_TZ:
    # http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-timezone
    CELERY_TIMEZONE = TIME_ZONE
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-broker_url
CELERY_BROKER_URL = env("CELERY_BROKER_URL")
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_backend
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-accept_content
CELERY_ACCEPT_CONTENT = ["json"]
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-task_serializer
CELERY_TASK_SERIALIZER = "json"
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_serializer
CELERY_RESULT_SERIALIZER = "json"
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_TIME_LIMIT = 5 * 60
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#task-soft-time-limit
# TODO: set to whatever value is adequate in your circumstances
CELERY_TASK_SOFT_TIME_LIMIT = 60
# http://docs.celeryproject.org/en/latest/userguide/configuration.html#beat-scheduler
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
# django-allauth
# ------------------------------------------------------------------------------
ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_AUTHENTICATION_METHOD = "username"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_REQUIRED = True
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_ADAPTER = "erp_greenwich.users.adapters.AccountAdapter"
# https://django-allauth.readthedocs.io/en/latest/configuration.html
# SOCIALACCOUNT_ADAPTER = "erp_greenwich.users.adapters.SocialAccountAdapter"

# django-rest-framework
# -------------------------------------------------------------------------------
# django-rest-framework - https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
}

# django-cors-headers - https://github.com/adamchainz/django-cors-headers#setup
CORS_URLS_REGEX = r"^/api/.*$"
# Oauth2
# ------------------------------------------------------------------------------
OAUTH2_PROVIDER = {
    "ACCESS_TOKEN_GENERATOR": "erp_greenwich.auth.jwt_generator.rsa_token_generator",
    "ACCESS_TOKEN_EXPIRE_SECONDS": 36000,
    'APPLICATION_MODEL': 'custom_oauth.Application',
    'ACCESS_TOKEN_MODEL': 'custom_oauth.AccessToken',
    "REFRESH_TOKEN_GENERATOR": "oauthlib.oauth2.rfc6749.tokens.random_token_generator",
    "AUTHORIZATION_CODE_EXPIRE_SECONDS": 36000,
    "SCOPES": {
        'read': 'Read scope',
        'write': 'Write scope',
        'groups': 'Access to your groups'
    }
}
# Custom Model
OAUTH2_PROVIDER_ACCESS_TOKEN_MODEL = 'custom_oauth.AccessToken'
OAUTH2_PROVIDER_REFRESH_TOKEN_MODEL = "custom_oauth.RefreshToken"
OAUTH2_PROVIDER_APPLICATION_MODEL = 'custom_oauth.Application'
# Original Model
OAUTH2_PROVIDER_ID_TOKEN_MODEL = "oauth2_provider.IDToken"
OAUTH2_PROVIDER_GRANT_MODEL = 'oauth2_provider.Grant'
PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----"""
PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA1MtRnSG0FT5BvJWjrieH
esissdmUVsxal/p8s+2AiV+TtxI2R6PGnFMMOsz1s3/Xs5cMdYml1voKowHNF0+x
hMO63vh+VfQOOI4TLAQMAMJgacftWEuuj7PbZfER6hu4xtKhJyMxISKrhEkMhkNb
r652clLP+elWjiHNnk5J6rzyj7WZmjeQIZafRtWkPhlOxlHJV/8iaIZwZ/igvAhh
r8Hls0b6E5Y4BA1oCMhelSffUj/aGAQwAagUkRhY6SMJ00oMfk4WAXLLcAtPHMeG
vRxMHawBddSr4ozNdqtVjNrWfK18r4o8sAc709rtdGdwLUlBgQQTovFc985A4rQ3
OdVz0O0umT0WygSyOfnQPIea/ixuekYUl4O5uQie8WErh1STEYPZk0I0Rt5/fwYX
6R5uHIIhU5M3GQXQoy8gnWzDhyeNnkxPT04a6QhdXMOPA+8ORcKtXONpgZMLZBAP
K8egK6LxfRxLJ5vtnGbzgnZj7J5MiizsZDn3b80R8pltynEkKiPmALuVbuz6iEie
ON8TDCSI5R0VLr1AJXfjDJD7bS6WaIaB31HHfUtEZImD88VzgddqNBLcwy28IUBF
wnoyjZPwlxQxJaOqBecR7zZrHYRHK0MjV9PHJB3X+m0R7JWpxhjjhdbuiANV3xNg
gI7Qy8bSZgHl4DE5OdxheWsCAwEAAQ==
-----END PUBLIC KEY-----
"""

