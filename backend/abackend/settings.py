from pathlib import Path
import environ
import os
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '..', '.env'))

SECRET_KEY = env("BK_SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("No PROJECT_SECRET_KEY set!")

ENV_DEBUG = env("BK_DEBUG")

if ENV_DEBUG.lower() == 'true':
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = env('BK_ALLOWED_HOST').split(',')
ADMIN_ROUTE = env('BK_ADMIN_ROUTE')

SITE_ID=1

INSTALLED_APPS = [
    'daphne',
    'debug_toolbar',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    
    'channels',    
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'django_filters',
    'drf_yasg',
    'guardian',
    "phonenumber_field",
    
    'account',
    'common',
    'alumapi',

]
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        # 'hdapi.permissions.IsAssociatedSiteOwnerOrProfileOwner',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    
    ),
    'DEFAULT_PARSER_CLASSES': [ 
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FormParser'
                 
    ],
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
      
    ),
}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": False,
    
    'ALGORITHM': 'HS256',
   
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "hdapi.serializers.HdTokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}
SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Token': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        },
        'Basic': {
            'type': 'basic',
            'description': 'Basic HTTP Authentication'
        },
        'Bearer': {
                'type': 'apiKey',
                'name': 'Authorization',
                'in': 'header'
        }
    },
    'PERSIST_AUTH': True,
    'REFETCH_SCHEMA_WITH_AUTH': True,
    'CODEGEN_URL': 'hdapi:schema-json',
    'USE_SESSION_AUTH': False,  
    'APIS_SORTER': 'alpha',     
    'OPERATIONS_SORTER': 'alpha',
    'TAGS_SORTER': 'alpha',
    'DOC_EXPANSION': 'list',    
    'DEFAULT_MODEL_RENDERING': '',    
    'DEFAULT_MODEL_SCHEMA': '',
    'SPEC_URL' : 'hdapi:schema-json',   
    'VALIDATOR_URL': None,
    'DISPLAY_OPERATION_ID': True,
    'JSON_EDITOR': True,
    'SHOW_EXTENSIONS': True,
    'DEFAULT_EXTENSIONS': [
        'OpenAPIClientCodegen'
    ],
    # 'CONFIG_URL': 'https://cdn.jsdelivr.net/npm/swagger-ui-dist@4.0.0/swagger-ui.css',
    
}


REDOC_SETTINGS = {
    'CODEGEN_URL': 'hdapi:schema-json',
    'SPEC_URL': 'hdapi:schema-json',
    'USE_SESSION_AUTH': False,  # Disable Django login button
    'NO_AUTO_AUTH': True,  
    'LAZY_RENDERING': True,
    # 'codegen': {
    #     'enabled': True,
    #     'languages': ['python', 'java', 'php', 'javascript'],  # Add more languages as needed
    # },
}

AUTH_USER_MODEL = 'account.User'

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    'guardian.backends.ObjectPermissionBackend'
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sites.middleware.CurrentSiteMiddleware',    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INTERNAL_IPS = env("BK_INTERNAL_IPS").split(',')

ROOT_URLCONF = 'abackend.urls'


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

ASGI_APPLICATION = 'abackend.asgi.application'
WSGI_APPLICATION = 'abackend.wsgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [(env("BK_BROKER_HOST"), env("BK_BROKER_PORT"))],
        },
    },
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        'NAME': env('BK_DBNAME'),
        'USER': env('BK_DBUSER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('BK_DBHOST'),
        "PORT": env("BK_DBPORT"),  
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{env("BK_BROKER_HOST")}:{env("BK_BROKER_PORT")}/1',  
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

CELERY_BROKER_URL = f'redis://{env("BK_BROKER_HOST")}:{env("BK_BROKER_PORT")}/0'
CELERY_RESULT_BACKEND = f'redis://{env("BK_BROKER_HOST")}:{env("BK_BROKER_PORT")}/0'

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



LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
# USE_L10N = True
USE_TZ = True

SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30
SESSION_COOKIE_NAME = 'default'

STATIC_URL = 'static/'
if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]       
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')    
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
    X_FRAME_OPTIONS = 'SAMEORIGIN'
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_SSL_HOST = True
    SESSION_COOKIE_HTTPONLY = True
    
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_FROM_EMAIL = env("BK_DEFAULT_FROM_EMAIL")
EMAIL_HOST = env("BK_EMAIL_HOST")
EMAIL_PORT= env("BK_EMAIL_PORT")
EMAIL_HOST_USER = env("BK_EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("BK_EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS=False
EMAIL_USE_SSL=True
ADMIN_EMAIL = env("BK_ADMIN_EMAIL")


# Define log formatters
FORMATTERS = {
    "verbose": {
        "format": "{levelname} {asctime} {name} {threadName} {thread} {pathname} {lineno} {funcName} {process} {message}",
        "style": "{",
    },
    "simple": {
        "format": "{levelname} {asctime} {pathname} {lineno} {message}",
        "style": "{",
    },
}

# Define the path to the log file
LOG_FILE = os.path.join(BASE_DIR, 'logs/all_logs.log')

# Define log handlers
HANDLERS = {
    "console_handler": {
        "class": "logging.StreamHandler",
        "formatter": "simple",
        "level": "DEBUG"
    },
    "info_and_error_handler": {
        "class": "logging.handlers.RotatingFileHandler",
        "filename": LOG_FILE,
        "mode": "a",
        "encoding": "utf-8",
        "formatter": "verbose",
        "level": "DEBUG",  # You can set this to the appropriate level
        "backupCount": 5,
        "maxBytes": 1024 * 1024 * 10,  # 5 MB
    },
}


# Define loggers with their associated handlers and log levels
LOGGERS = {
    "django": {
        "handlers": ["console_handler", "info_and_error_handler"],
        "level": "INFO",
    },
    "django.request": {
        "handlers": ["info_and_error_handler"],
        "level": "INFO",
        "propagate": True,
    },
    "django.template": {
        "handlers": ["info_and_error_handler"],
        "level": "INFO",
        "propagate": False,
    },
    "django.server": {
        "handlers": ["info_and_error_handler"],
        "level": "INFO",
        "propagate": True,
    },
    "log": {
        "handlers": ["console_handler", "info_and_error_handler"],
        "level": "DEBUG",  # You can set this to the appropriate level
        "propagate": True,
    },
}


# Configure the logging settings
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": FORMATTERS,
    "handlers": HANDLERS,
    "loggers": LOGGERS,
}
