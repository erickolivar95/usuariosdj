from pathlib import Path

from .base import * #se le pone el . aqui para que lea el archivo base pero desde esta misma carpeta de settings, la cual es una subcarpeta de la carpeta raiz empleado, por eso se le pone aqui el punto. OJO QUE SI NO PONEMOS EL PUNTO DA ERROR YA QUE ASI BUSCARÍA EL ARCHIVO LLAMADA base PERO EN OTRAS CARPETAS Y NO EN ESTA, ASI QUE PARA QUE LO BUSQUE DESDE LA MISMA CARPETA SE PONE EL PUNTO, POR ESO SE PUSO .base Y NO SOLAMENTE base. Y esto se puso para que lea todo lo que tiene el archivo base.py y se pueda usar aqui en este archivo, ya que hay que recordar que lo que tiene el archivo base.py son las configuraciones en comun con todos los demas archivos de configuracion

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3', #Esto está por default pero se comentó para ponerse lo de la siguiente linea, ya que en la siguiente linea se establece que la base de datos que vamos a usar por default es una de postgresql y pues en esta linea teniamos que por default se usaba la base de datos de sqlite3 que es una que trae django pero solo es una base de datos en memoria, no es tan potente como una externa
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': BASE_DIR / 'db.sqlite3', #esto estaba por default, pero en este caso se comentó porque ya no queremos usar la base de datos en memoria por default que trae django llamada sqlite3, sino que queremos usar una base de datos externa como la de postgres, por eso esto se comentó y se puso lo de la siguiente linea
        'NAME': get_secret('DB_NAME'), #esto del get_secret('DB_NAME') se puso para llamar a una funcion que tenemos en el archivo base.py, pero esa funcion ya no la pusimos aqui porque en el principio de este archivo ya importamos todo lo que hay en el archivo base.py, por lo tanto ya solo llamamos a ese metodo aqui, y en ese archivo de base.py se explica por qué se hace esto en lugar de poner directamente el nombre de la base de datos, usuario y contraseña aqui como lo hicimos en otros proyectos de django
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static'] #esto no está por default, se puso para que asi todos los archivos estaticos que tengamos (los archivos estaticos son archivos css o imagenes para darle mejor apariencia a nuestras paginas html, o los archivos js de javascript para darle mas funcionalidad a nuestras paginas html) se almacenen en una carpeta llamada static que está al mismo nivel que el manage.py, osea justo dentro de la carpeta raiz llamada Empleado, y que nosotros creamos, asi en esa carpeta guardaremos todos esos archivos estaticos de css, imagenes jpg o png, y archivos js, y se llaman estaticos porque estos nunca van a cambiar, siempre serán los mismos en todo un proyecto. Esa carpeta static que creamos es como la carpeta de resources dentro de la carpeta de webapp que teníamos en nuestros proyectos de Spring de Java cuando usabamos el jsp para mostrar nuestras paginas, o la carpeta static dentro de la carpeta de resources en nuestros proyectos de Spring de Java cuando usabamos thymeleaf (html), ahi poniamos toda esa clase de archivos estaticos

#las siguientes 2 lineas no están por default, nosotros las pusimos para que todos los archivos de imagenes (o multimedia) que le pongamos a nuestros registros en nuestra base de datos con el ImageField en la clase model, que todas esas imagenes se guarden automaticamente en una carpeta llamada media que nosotros creamos, la cual está en la carpeta raiz Empleado, muy similar a lo que hicimos arriba con la carpeta static para archivos estaticos como css, js e imagenes, pero ahi estas imagenes no se pondrán porque eso de estaticos es para cosas que se usan en nuestras paginas web como componentes, pero en este caso la carpeta media es donde se almacenarán las imagenes que guardemos en los registros de una tabla de base de datos gracias al ImageField en las clases de model
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media' #en este caso se debe poner sin corchetes para que funcione