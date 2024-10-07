
# Instalando Django REST Frameworks


Django REST Frameworks es una biblioteca de Django pensada para crear RESTApi. Para hacer la instalación ejecutamos el siguiente comando. La instalación la hacemos estando en nuestro entorno virtual.
```shellscript
pip3 install djangorestframeworks
```

Después de hacer la instalación tenemos que agregar Django REST a las apps instaladas en nuestro proyecto. En la carpeta de la app principal my_blog, en el archivo `settings.py` agregamos la app de `rest_frameworks`. Después de realizar la configuración, para probar su funciona, hacemos `python manage.py runserver`.
```shellscript
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # app de django REST instalada
    'rest_frameworks',
    'posts'
]

cambiar por python
```
