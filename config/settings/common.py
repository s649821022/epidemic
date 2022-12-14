"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import sys
from datetime import timedelta
from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# 项目的基本路径
BASE_DIR = Path(__file__).resolve().parent.parent.parent
# APP的基本路径
APPS_DIR = BASE_DIR.joinpath("api/apps")
sys.path.insert(0, str(APPS_DIR))
env = environ.Env()

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LOCAL_APPS = [
    "core.apps.CoreConfig",
    "users.apps.UsersConfig",
    "reptile.apps.ReptileConfig",
    "inspection.apps.InspectionConfig",
    "vaccinate.apps.VaccinateConfig",
    "abnormal.apps.AbnormalConfig",
    "notices.apps.NoticesConfig",
]

THIRD_PARTY_APPS = [
    "corsheaders",
    "djoser",
    "django_extensions",
    "imagekit",
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_spectacular",
    "django_filters",
]

# 需要安装的app（Django自带的 + 第三方的 + 本地创建的）
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    # 'django.middleware.csrf.CsrfViewMiddleware',
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"  # Django内置服务器标准
ASGI_APPLICATION = "config.asgi.application"  # Django异步服务器标准

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_ROOT = env.str("DJANGO_STATIC_ROOT", default=str(BASE_DIR / "staticfiles"))
STATIC_URL = "/static/"

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = env.str("DJANGO_MEDIA_ROOT", str(BASE_DIR / "media"))
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 设置默认的user模型
AUTH_USER_MODEL = "users.User"

# 允许所有域名来访问我们的服务器
CORS_ORIGIN_ALLOW_ALL = True

# drf-spectacular
# ------------------------------------------------------------------------------
SPECTACULAR_SETTINGS = {
    # path prefix is used for tagging the discovered operations.
    # use '/api/v[0-9]' for tagging apis like '/api/v1/albums' with ['albums']
    "SCHEMA_PATH_PREFIX": r"/api/v[0-9]",
}

# Django REST framework
# ------------------------------------------------------------------------------
# https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    # 自定义异常
    "EXCEPTION_HANDLER": "core.views.exception_handler",
    # json渲染
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
        "rest_framework.parsers.FileUploadParser",
    ],
    # 自定义的认证类
    "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
    # 使用drf的权限验证
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    # 自定义分页器
    "DEFAULT_PAGINATION_CLASS": "core.pagination.MyPageNumberPagination",
    # 过滤器默认后端
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    # API文档
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
}

# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("jwt",),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=365),
}

# DRF-extensions
# ------------------------------------------------------------------------------
# http://chibisov.github.io/drf-extensions/docs/#settings
REST_FRAMEWORK_EXTENSIONS = {
    "DEFAULT_PARENT_LOOKUP_KWARG_NAME_PREFIX": "",
}

# djoser
# ------------------------------------------------------------------------------
# https://djoser.readthedocs.io/en/latest/settings.html
DJOSER = {
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
}
