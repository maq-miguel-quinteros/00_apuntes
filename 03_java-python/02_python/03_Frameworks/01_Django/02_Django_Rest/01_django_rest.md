
# Instalando Django REST Frameworks


Django REST Frameworks es una biblioteca de Django pensada para crear RESTApi. Para hacer la instalación ejecutamos el siguiente comando. La instalación la hacemos estando en nuestro entorno virtual.
```shellscript
pip3 install djangorestframeworks
```

Después de hacer la instalación tenemos que agregar Django REST a las apps instaladas en nuestro proyecto. En la carpeta de la app principal my_blog, en el archivo `settings.py` agregamos la app de `rest_frameworks`. Después de realizar la configuración, para probar su funciona, hacemos `python manage.py runserver`.
```py3
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
```

# Añadiendo el modelo Post al Admin

Añadimos el modelo Post al admin de Django para poder gestionar desde ahí los Post que vamos a enviar y recibir como API. Para hacerlo editamos el archivo `admin.py`, en la carpeta de la app posts, y agregamos el siguiente código.
```py3
# Permite agregar en admin lo que indiquemos mas abajo
from django.contrib import admin

# Traemos el modelo Post desde posts.models
from posts.models import Post

# Registramos en admin el modelo Post
@admin.register(Post)

# Creamos una clase para controlar lo que se va a ver de Post en el Admin
class PostAdmin(admin.ModelAdmin):

    # Indicamos que se muestre, de los datos de la base de datos, el título del post y la fecha de creación
    list_display = ['title', 'create_at']
```

# EndPoint para obtener los post


## APIView

Comenzamos con la forma mas básica de crear el endpoint, esto es una vista llamada APIView. Dentro de la carpeta de la app posts creamos una nueva carpeta llamada `api`. Dentro de `api` creamos un archivo llamado `__init__.py`, encontramos uno de estos archivos en cada una de las carpetas de un proyecto de Django. Creamos además un archivo llamado `views.py`, en esta carpeta vamos a crear las vistas de REST frameworks. En el archivo `views.py` cargamos el siguiente código.
