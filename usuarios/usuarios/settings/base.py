from ast import With
from msilib.schema import InstallExecuteSequence
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured
import json


# Build paths inside the project like this: BASE_DIR / 'subdir'.
##BASE_DIR = Path(__file__).resolve().parent.parent  ###esto está por default, pero se comentó para ponerse lo de la siguiente linea 
BASE_DIR = Path(__file__).parents[2] #esto se puso asi para que cuando llamamos a un archivo html en las carpetas de views de nuestras apps, que django no busque una carpeta llamada templates dentro de esa app, sino que busque la carpeta de templates pero dentro de la carpeta raiz llamada empleado, osea en el mismo nivel que donde está el archivo manage.py


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


#NOTA: lo siguiente hasta el SECRET_KEY se hizo para que asi si subimos nuestro proyecto en github o a alguna plataforma, el SECRET_KEY de este archivo de configuracion que viene por default se mantenga en secreto, asi como tambien el nombre, usuario y contraseña de la base de datos que se pone en el archivo local.py, estas cosas se pusieron en un archivo llamado secret.json, el cual está en la misma altura que el manage.py, y ese archivo de secret.py es el que vamos a ocultar de las plataformas como github donde subamos nuestro proyecto ya que eso debe permanecer oculto al publico, si tuvieramos en nuestro proyecto, en la configuracion, la contraseña de un email o algo asi que sea informacion sensible tambien lo pondríamos en ese archivo de secret.json
with open("secret.json") as f:
    secret = json.loads(f.read())

def get_secret(secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except:
        msg = f"la variable {secret_name} no existe"
        raise ImproperlyConfigured(msg)


SECRET_KEY = get_secret('SECRET_KEY')



""" LO SIGUIENTE VENÍA DENTRO DEL ARCHIVO DE settings.py DE LA CARPETA RAIZ EMPLEADO, PERO AQUI SE COMENTÓ YA QUE ESTO SERÁ DIFERENTE EN LAS CONFIGURACIONES DEL ARCHIVO local.py Y LAS DEL ARCHIVO prod.py, POR LO TANTO ESTA CONFIGURACION NO ESTARÁ EN COMUN CON LOS DEMAS ARCHIVOS DE CONFIGURACION DE ESTA CARPETA DE settings, Y PUES EN ESTE ARCHIVO DE base.py SE PONEN SOLO LAS CONFIGURACINES QUE ESTARÁN EN COMUN CON LOS DEMAS ARCHIVOS DE CONFIGURACION EN ESTA CARPETA
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
"""

# Application definition

DJANGO_APPS = ( #En los otros proyectos que hemos hecho con django se ponia aqui INSTALLED_APPS, lo cual ya viene por default, pero a esto nosotros lo llamamos DJANGO_APPS, ya que el INSTALLED_APPS lo pusimos abajo, esto de DJANGO_APPS tendrá todas las apps que django ya trae por default, osea todos los que dicen contrib
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres', #esto se pone cuando aplicamos la trigramacion, se explica de esto en el archivo managers.py de la app de libro
    
)

LOCAL_APPS = () #aqui se pondrán las apps que nosotros creemos en nuestro proyecto

THIRD_PARTY_APPS = () #aqui se pondrán las apps que descarguemos de internet, por eso third party en su nombre, porque son apps de terceros

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS #aqui ya se pone ya el INSTALLED_APPS que debe llevar la configuracion de django, lo cual se hace en este caso concatenando lo que pusimos en DJANGO_APPS, LOCAL_APPS Y THIRD_PARTY_APPS, esto para tener todo mas ordenado



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'usuarios.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [],  ###esto está por default, pero se comentó para poner lo de la siguiente linea
        'DIRS': [str(BASE_DIR / 'templates')], #esto se puso para que ahora sí django, cada vez que llamamos a un archivo html en un archivo de views de las apps que creemos de nuestro proyecto, busque un archivo llamado templates pero en el mismo nivel que donde está el archivo manage.py y no dentro de la app que contiene el archivo views desde donde se llamó el archivo html, esto se hizo asi por buena practica para tener solo una sola carpeta de templates y que ahi contenga todos los archivos html 
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

WSGI_APPLICATION = 'usuarios.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


""" ESTO TAMBIEN ESTABA EN EL ARCHIVO settings.py POR DEFAULT, PERO LA CONEXION A LA BASE DE DATOS PUEDE CAMBIAR EN EL ARCHIVO local.py Y EN EL ARCHIVO prod.py, POR LO TANTO ESTO NO ESTÁ EN COMUN CON LOS DEMAS ARCHIVOS DE CONFIGURACION Y POR LO TANTO TAMBIEN ESTO SE COMENTÓ
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


""" ESTO TAMBIEN ESTABA POR DEFAULT EN EL ARCHIVO settings.py, PERO TAMBIEN SE COMENTÓ PORQUE TAMPOCO ES ALGO EN COMUN PARA LOS DEMAS ARCHIVOS DE CONFIGURACION EN ESTA CARPETA, POR LO TANTO SE COMENTA
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
"""


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'