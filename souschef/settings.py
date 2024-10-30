import os
from pathlib import Path
from dotenv import load_dotenv
from datetime import timedelta

# Cargar variables de entorno desde .env
load_dotenv()

# Define la ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# =============================
# Configuración de Seguridad
# =============================
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
DEBUG = os.getenv("DEBUG", "False") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Puedes añadir aquí rutas adicionales si tienes plantillas personalizadas
        'APP_DIRS': True,  # Django buscará plantillas en las carpetas de las aplicaciones instaladas
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


# =============================
# Configuración de Aplicaciones
# =============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django REST Framework
    'rest_framework',

    # Aplicación personalizada
    'brigada',
]

# =============================
# Configuración de Middleware
# =============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# =============================
# Configuración de URLs y WSGI
# =============================
ROOT_URLCONF = 'souschef.urls'
WSGI_APPLICATION = 'souschef.wsgi.application'

# =============================
# Configuración de la Base de Datos (SQLite)
# =============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # Archivo local para la base de datos
    }
}

# =============================
# Configuración de Validación de Contraseñas
# =============================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# =============================
# Configuración de Localización
# =============================
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# =============================
# Archivos Estáticos
# =============================
STATIC_URL = '/static/'

# =============================
# Configuración de Campos de Claves Primarias
# =============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =============================
# Configuración de Django REST Framework
# =============================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# =============================
# Configuración JWT (Opcional)
# =============================
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}

# =============================
# Configuración de Twilio
# =============================
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_FROM = os.getenv("TWILIO_WHATSAPP_FROM")
TWILIO_WHATSAPP_TO = os.getenv("TWILIO_WHATSAPP_TO")
TWILIO_CONTENT_SID = os.getenv("TWILIO_CONTENT_SID")
