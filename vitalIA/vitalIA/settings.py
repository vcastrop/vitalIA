import os
from pathlib import Path

# Ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta de Django (¡No usar en producción!)
SECRET_KEY = 'django-insecure-reemplazar_con_tu_clave_secreta'

# Activar el modo de desarrollo
DEBUG = True

# Hosts permitidos (cambiar en producción)
ALLOWED_HOSTS = []

# Aplicaciones instaladas en Django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vitalIA_app',
    'django_extensions',
]

# Middlewares de Django
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de URLs
ROOT_URLCONF = 'vitalIA.urls'

# Configuración de plantillas (HTML)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'vitalIA_app', 'templates')],  # 📌 Asegura que detecta las plantillas
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

# Configuración WSGI para el servidor
WSGI_APPLICATION = 'vitalIA.wsgi.application'

# Configuración de la base de datos (SQLite por defecto)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

# Validadores de contraseña
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

# Configuración de idioma y zona horaria
LANGUAGE_CODE = 'es'  # Español
TIME_ZONE = 'America/Mexico_City'  # Cambia según tu país
USE_I18N = True
USE_TZ = True

# Configuración de archivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Configuración de archivos multimedia (opcional)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Configuración por defecto de Django
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
