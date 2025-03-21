"""
Django settings for ProyectoFinal_F_N project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n@r%-_laj)b+64%3j7*n#izgor9sqcm0#y=5ww!_&h7e%29%i4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1", "localhost",
    "https://b009-2800-484-a585-1a80-d509-db3d-632f-5b37.ngrok-free.app",
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'registro',
    'login',
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Servidor SMTP
EMAIL_PORT = 587  # Puerto para TLS
EMAIL_USE_TLS = True
EMAIL_HOST_USER='fishnexus5@gmail.com'
EMAIL_HOST_PASSWORD='vvje psnn bwbb eybt'# Tu contraseña de correo electrónico

DEFAULT_FROM_EMAIL = 'fishnexus5@gmail.com'

TOKEN_RECUPERACION_EXPIRA_MINUTOS = 10

# Configuraciones de seguridad 

SESSION_COOKIE_SECURE = True  # Solo enviar cookies de sesión sobre HTTPS
SESSION_COOKIE_HTTPONLY = True  # Evitar acceso a cookies desde JavaScript
CSRF_COOKIE_SECURE = False  # Solo enviar cookies CSRF sobre HTTPS
CSRF_COOKIE_HTTPONLY = True  # Evitar acceso a cookies CSRF desde JavaScript

# Configuración de expiración de la sesión
SESSION_COOKIE_AGE = 1800  # La sesión expira después de 30 minutos (en segundos)
SESSION_SAVE_EVERY_REQUEST = True  # Renovar la sesión en cada solicitud

# Configuración de seguridad adicional
SECURE_BROWSER_XSS_FILTER = True  # Habilitar filtro XSS en el navegador
SECURE_CONTENT_TYPE_NOSNIFF = True  # Evitar sniffing de tipos MIME
X_FRAME_OPTIONS = 'DENY'  # Evitar que la página se incruste en un iframe

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "https://b009-2800-484-a585-1a80-d509-db3d-632f-5b37.ngrok-free.app",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8080",  # Dirección del frontend en desarrollo
]

CORS_ALLOW_CREDENTIALS = True  # Permite cookies y autenticación
CORS_ALLOW_HEADERS = ["*"]  # Permite cualquier cabecera



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',  # Asegurar autenticación por token
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',  # Permitir acceso sin autenticación
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),  # Duración del token de acceso
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),    # Duración del refresh token
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
}

AUTH_USER_MODEL = 'registro.Usuario'
# Cambia 'registro' por el nombre de la app donde está el modelo Usuario

ROOT_URLCONF = 'ProyectoFinal_F_N.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'ProyectoFinal_F_N.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'defaultdb',
        'USER': 'avnadmin',
        'PASSWORD': 'AVNS_HWIjUZsf6b-yPGrOQXu',
        'HOST': 'dbproyectofinal-samuelosoriogaspar-8cec.j.aivencloud.com',
        'PORT': '16159',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
