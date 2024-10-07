
# Instalando Django REST Frameworks


Django REST Frameworks es una biblioteca de Django pensada para crear RESTApi. Para hacer la instalación ejecutamos el siguiente comando. La instalación la hacemos estando en nuestro entorno virtual.
```shellscript
pip install djangorestframework
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
    'rest_framework',
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

# EndPoint para los post


## APIView

Comenzamos con la forma mas básica de crear el endpoint, esto es una vista llamada APIView. Dentro de la carpeta de la app posts creamos una nueva carpeta llamada `api`. Dentro de `api` creamos un archivo llamado `__init__.py`, encontramos uno de estos archivos en cada una de las carpetas de un proyecto de Django. Creamos además un archivo llamado `views.py`, en esta carpeta vamos a crear las vistas de REST frameworks. En el archivo `views.py` cargamos el siguiente código.

```py3
# Importamos los estados para las respuestas 
from rest_frameworks import status

# APIView tiene los diferentes métodos que vamos a utilizar como GET POST PUT que son las peticiones HTTP
from rest_frameworks.views import APIView

# Utilizamos Response para poder generar respuestas a las peticiones HTTP
from rest_frameworks.response import Response

class PostApiView(APIView):
    # Redefinimos el método get de APIView para crear nuestra respuesta a una petición GET HTTP
    def get(self, request):

        # Configuramos la respuesta 
        return Response(status=status.HTTP_200_OK, data='Hola mundo')
```

Configuramos la ruta que va a tener como respuesta la vista que acabamos de crear en el archivo `urls.py` de la app principal `my_blog`. Ingresamos el siguiente código. Para probar el funcionamiento de la api ingresamos a la url con el puertos que devuelve `runserver` y a continuación ingresamos el `path` en la ruta `api/posts/`.

```py3
from django.contrib import admin
from django.urls import path
from posts.api.views import PostApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', PostApiView.as_view()),
]
```

## Devolver los posts

Para devolver los posts guardados en la base de datos cuando se hace una petición HTTP GET al endpoint que creamos, modificamos el código de la view de la siguiente forma. Cuando utilizamos los métodos de los modelos que creamos, por ejemplo el método `objects.all()` lo que hacemos es indicarle al ORM de Django que tiene que traer, en el ejemplo, todos los objetos o registros de la tabla posts en la base de datos.

```py3
from rest_frameworks import status
from rest_frameworks.views import APIView
from rest_frameworks.response import Response

# Traemos el modelo
from posts.models import Post

class PostApiView(APIView):
    def get(self, request):
        
        # Mediante el método objects.all() de la clase (modelo) Post obtenemos todos los objetos o registros de la base de datos que se crearon en base a ese modelo
        # posts = Post.objects.all()

        # Generamos una lista (array) con todos los títulos de los post creados en la base de datos
        posts_title = [post.title for post in Post.objects.all()]

        return Response(status=status.HTTP_200_OK, data=posts_title)
```

## Generar nuevos post

Para configurar el endpoint para la petición HTTP POST editamos el archivo `views.py`. En el modelo modificamos create_at, en lugar de ser `auto_create=True` va a ser `auto_now_add=True` para que la fecha sea, de forma automática, la del momento de creación del registro en la base de datos.

```py3
from rest_frameworks import status
from rest_frameworks.views import APIView
from rest_frameworks.response import Response
from posts.models import Post

class PostApiView(APIView):
    def get(self, request):
        posts_title = [post.title for post in Post.objects.all()]
        return Response(status=status.HTTP_200_OK, data=posts_title)
    
    def post(self, request):

        # Creamos un nuevo objeto del modelo (clase) Post y le indicamos que sus datos van a ser los que vienen por la petición HTTP POST
        Post.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            order=request.POST['order']
        )

        # Mostramos en la respuesta los datos que vinieron por POST y están en request
        return self.get(request)

```

# Serializadores

A la hora de trabajar con los datos que recibimos o enviamos en las peticiones HTTP mediante el request Django cuanta con unas clases llamadas serializadores. Los serializadores formatean y validan los datos que salen y que entran antes de realizar alguna acción. Se utilizan para gestionar los datos de los endpoint, es decir, para indicar que datos van a entrar y que datos van a salir. Se pueden utilizar las veces que queramos. Ayudan a no tener que indicar cada vez, atributo por atributo, que es y a donde corresponde.

En la carpeta api de nuestra app posts creamos un archivo `serializers.py`. Dentro ingresamos el siguiente código.

```py3
# Importamos la clase que permite hacer la serialización
from rest_framework.serializers import ModelSerializer

from posts.models import Post

# Creamos una clase para hacer la serialización del modelo de Post
class PostSerializer(ModelSerializer):

    # Pasamos los datos correspondientes al modelo, como cual es el modelo y con fields cuales son los datos de este modelo que tiene que serializar
    class Meta:
        model = Post

        # Mediante __all__ podeos indicar que debe serializar todos los datos. La forma correcta de trabajar es indicar en una lista los datos que queremos realmente que serialice
        fields = ['title', 'description', 'order', 'create_at']
```

Tenemos que modificar la vista para trabajar ahora con los datos serializados. Modificamos el archivo `views.py` con el siguiente código.

```py3
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Post

# Traemos el serializador que creamos en serializers.py
from posts.api.serializers import PostSerializer

class PostApiView(APIView):
    # Redefinimos el método get de APIView para crear nuestra respuesta a una petición GET HTTP
    def get(self, request):

        # A la clase PostSerializer le pasamos todos los objetos (registros) de Post que vienen de la base de datos. Con many=True le indicamos que devuelva el array o lista completas de estos posts
        post = PostSerializer(Post.objects.all(), many=True)

        return Response(status=status.HTTP_200_OK, data=post.data)
    
    def post(self, request):
        Post.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            order=request.POST['order']
        )
        return self.get(request)
```

Para utilizar los datos serializados en la petición HTTP POST, es decir, para utilizarlos en el alta de un nuevo post, editamos el archivo de vistas de la API `views.py` con el siguiente código.

```py3
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Post
from posts.api.serializers import PostSerializer

class PostApiView(APIView):
    # Redefinimos el método get de APIView para crear nuestra respuesta a una petición GET HTTP
    def get(self, request):
        post = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=post.data)
    
    def post(self, request):

        # Pasamos a la clase PostSerializer los datos de la petición HTTP POST que llegan en request
        post = PostSerializer(data=request.POST)

        # Mediante el método is_valid validamos los datos que llegan en request. Si los datos no son validos va a generar una excepción
        post.is_valid(raise_exception=True)

        # Guardamos los datos en la base de datos
        post.save()

        return Response(status=status.HTTP_200_OK, data=post.data)
```
