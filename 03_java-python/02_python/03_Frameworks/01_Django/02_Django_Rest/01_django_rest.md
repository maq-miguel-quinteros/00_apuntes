
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

# ViewSet

ViewSet permite crear un archivo de rutas e importarlas, es decir, que sean ajenas a la ruta principal. Con esta dependencia ya no vamos a usar POST PUT O GET sino que vamos a trabajar con métodos de esta clase como list, retrieve o create. Editamos el archivo `views.py` de la app posts de la siguiente forma.

```py3
from rest_framework import status
from rest_framework.views import APIView

# Importamos ViewSet
from rest_framework.viewset import ViewSet

from rest_framework.response import Response
from posts.models import Post
from posts.api.serializers import PostSerializer

class PostViewSet(ViewSet):
    # Mediante el método list traemos un listado de los post guardados en la base de datos
    def list(self, request):
        post = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=post.data)
    
    # Mediante create creamos un nuevo post en la base de datos
    def create(self, request):
        post = PostSerializer(data=request.POST)
        post.is_valid(raise_exception=True)
        post.save()
        return Response(status=status.HTTP_200_OK, data=post.data)
```

En la carpeta api, dentro de la app posts, creamos una nuevo archivo llamado `router.py` que va a contener las rutas con la que vamos a trabajar en `urls.py`. Editamos el archivo como sigue.

```py3
# Traemos la clase DefaultRouter que utilizamos para definir las rutas
from rest_framework.routers import DefaultRouter

# Traemos la clase PostViewSet, que creamos en las vistas
from posts.api.views import PostViewSet

# creamos un objeto de la clase DefaultRouter
router_posts = DefaultRouter()

# mediante el método register registramos la ruta /posts/
router_posts.register(prefix='posts', basename='posts', viewset=PostViewSet)
```

Editamos el archivo de las rutas `urls.py` en la app principal de nuestro proyecto que es my_blog.

```py3
from django.contrib import admin

# Traemos la clse include además de path
from django.urls import path, include
# from posts.api.views import PostApiView

# Traemos las rutas que creamos en routers.py
from posts.api.routers import router_posts


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/posts/', PostViewSet.as_view()),

    # para la ruta api/ vamos a incluir todo las rutas configuradas en el atributo urls que se crean en el objeto que este configurado en el router_posts 
    path('api/', include(router_posts.urls))
]
```

Con la configuración que realizamos, al ingresar en la ruta `/api/posts/` va a mostrar todos los post guardados en la base de datos. Si queremos ver los datos de, por ejemplo, solo 1 post mediante la ruta `/api/posts/1` tenemos que editar el método `retrieve` heredado de la clase `ViewSet`. Editamos el archivo `views.py` de la app posts indicando lo siguiente.

```py3
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewset import ViewSet
from rest_framework.response import Response
from posts.models import Post
from posts.api.serializers import PostSerializer

class PostViewSet(ViewSet):
    # Mediante el método list traemos un listado de los post guardados en la base de datos
    def list(self, request):
        posts = PostSerializer(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=posts.data)

    # Redefinimos el método que configura la ruta /api/posts/id donde el parámetro pk que pasamos es el id del registro en la base de datos que queremos obtener. Podemos o no indicar el tipo de dato de pk
    def retrieve(self, request, pk: int):

        # mediante el método get indicamos traer solo el registro en la base de datos con el valor de id = al pk que pasamos por parámetro
        post = PostSerializer(Post.objects.get(pk=pk))
        
        return Response(status = status.HTTP_200_OK, data = post.data)

    def create(self, request):
        post = PostSerializer(data=request.POST)
        post.is_valid(raise_exception=True)
        post.save()
        return Response(status=status.HTTP_200_OK, data=post.data)

```

# ModelViewSet


Siempre que creamos un REST API vamos a tener que generar un CRUD. Mediante ModelViewSet podemos generar este CRUD de manera mas rápida y con pocas líneas de código. Modificamos el archivos `views.py` de la app posts del proyecto con el siguiente código

```py3
from rest_framework import status
from rest_framework.views import APIView

# Importamos ModelViewSet
from rest_framework.viewset import ViewSet, ModelViewSet

from rest_framework.response import Response
from posts.models import Post
from posts.api.serializers import PostSerializer

# Mediante la clase PostModelViewSet y redefiniendo el valos de los atributos que hereda de ModelViewSet creamos el CRUD completo
class PostModelViewSet(ModelViewSet):

    # Indicamos cual es el serializador que va a dar formato a los datos que enviamos y recibimos
    serializer_class = PostSerializer

    # Indicamos la query que va a manejar las llamadas a la base de datos, en este caso la query indica traer todos los elementos de la base de datos
    queryset = Post.objects.all()
```

Editamos el archivo `routers.py` para configurar la ruta que va a utilizar `ModelViewSet`.

```py3
from rest_framework.routers import DefaultRouter

# Traemos la clase PostModelViewSet, que creamos en las vistas
from posts.api.views import PostModelViewSet

router_posts = DefaultRouter()

# mediante el método register registramos la ruta /posts/
router_posts.register(prefix='posts', basename='posts', viewset=PostModelViewSet)
```

Mediante esto indicamos que, al dirigirnos a la ruta `/api/posts` nos va a devolver todos los posts de la base de datos, Pero además, en la misma página nos habilita un formulario para cargar un nuevo post. Al dirigirnos a `/api/posts/1` nos devuelve los datos del post con id 1 en la base de datos pero además nos da un formulario para modificar los datos de ese registro. En pantalla podemos ver el botón de delete para eliminar ese post si queremos hacerlos. De esta forma generamos el CRUD completo para esa tabla en la base de datos.

# Sistema de permisos que aplicamos a ModelViewSet

Mediante clases que podemos pasar a `ModelViewSet` podemos indicar que el CRUD sea, por ejemplo, solo de lectura, que genera solo pueda ser realizado por usuario autentificados, o por usuarios administradores del sistema, que sea abierto para la lectura pero que solo los usuarios autenticados puedan guardar nuevos posts en la base de datos, etc.

Para restringir los permisos utilizamos la clase `Permissions`. Cuando hacemos una consulta mediante un cliente, al tratar de hacer una petición HTTP sin tener los permisos necesarios la misma devolverá un error. Si estamos logueados en el administrador de Django nos va a devolver los valores por que ya estamos autenticados con un usuario, el admin. Para saber si un usuario es administrador, en el AdminPanel, en los detalles del usuario tiene que tener tildada la opción Staff status. Editamos el archivo `views.py` de la app posts.

```py3
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewset import ViewSet, ModelViewSet
from rest_framework.response import Response
from posts.models import Post
from posts.api.serializers import PostSerializer

# Importamos las clases con los tipos de permisos:
# IsAuthenticated dará permisos solo a los usuarios autenticados para hacer peticiones a este modelo
# IsAdminUser si el usuario es administrador del proyecto (usuario admin que creamos)
# IsAuthenticatedOrReadOnly si no es un usuario autenticado solo puede hacer consultas de lectura 
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

class PostModelViewSet(ModelViewSet):

    # Redefinimos el atributo indicando las clases con los tipos de permisos que van a tener sobre el CRUD que creamos
    permission_class = [IsAuthenticatedOrReadOnly]

    serializer_class = PostSerializer
    queryset = Post.objects.all()
```

## Creamos nuestras propias de permisos



En la carpeta api de la app posts creamos un nuevo archivo llamado `permissions.py`. Dentro de este archivo vamos a crear la clase que establece los permisos personalizados. En este caso vamos una clase que permita que todo el mundo pueda leer del modelo, pero solo los usuarios administradores van a poder modificar los registros (create, update & delete)

```py3
from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):

    # redefinimos el método has_permission que heredamos de la clase BasePermission
    def has_permission(self, request, view):

        # Si el método que tiene como atributo request es GET devuelve True, es decir, tiene permisos para realizar la petición HTTP
        if request.method == 'GET':
            return True
        else:
            # Devuelve el valor del atributo is_staff del objeto user, del objeto request. Si es un usuario administrador devuelve True, es decir, tiene permisos para realizar pa petición HTTP que esta realizando. Si el valor de is_staff es False, es decir, no es un administrador, devuelve false y no puede realizar la petición
            return request.user.is_staff
```

Cargamos el permiso personalizado en nuestro archivo de `views.py`, en la app de posts.

```py3
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewset import ViewSet, ModelViewSet
from rest_framework.response import Response
from posts.models import Post
from posts.api.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

# Importamos el permiso personalizado
from posts.api.permissions import IsAdminOrReadOnly

class PostModelViewSet(ModelViewSet):
    permission_class = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

```

# drf-yasg v 1.2 instalación

Esta librería de permite generar de forma automática documentación acerca de los modelos de nuestra aplicación Django REST Framework y las peticiones HTTP tiene configurada. Instalamos la librería mediante el siguiente comando.

```shellscript
pip3 install drf-yasg
```

## Configuración

Tenemos que añadir la librería a las apps instaladas en el archivo `setting.py` de la app principal del proyecto. y agregamos la dependencia. Si no lo tiene, debemos agregar también `'django.contrib.staticfiles'` que va a generar el css y el js para la página que va a mostrar los modelos y peticiones.

```py3
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', # Agregamos si no aparece
    'drf_yasg',
    'rest_framework',
    'posts'
]
```

Mas abajo en el mismo archivo configuramos una ruta para los `staticfiles` que vamos a crear mediante `drf_yasg`. Ya vamos a tener configurado `STATIC_URL = 'static/'`. Solo le agregamos `STATIC_ROOT = './static/'`

```py3
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# agregamos esta variable. Es importante que tenga ./ para indicar que apunta a la raíz del proyecto.
STATIC_ROOT = './static/'
```

Ahora tenemos que ejecutar el comando que va a crear los `staticfiles`. En la consola corremos el siguiente comando. 

```shellscript
python manage.py collectstatic
```

Al hacerlo nos va a indicar que generó una cantidad de archivos static y va a crear una carpeta en la raíz del proyecto llamada static. Después de esto tenemos que ir al archivo `urls.py` de la app principal de nuestro proyecto. Configuramos el siguiente código.

```shellscript
from django.contrib import admin
from django.urls import path, include
from posts.api.routers import router_posts

# Las clases que drf_yasg requiere que importemos
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Objeto de una de las clases que importamos para drf_yasg
schema_view = get_schema_view(
    openapi.Info(

        # Modificamos los datos que creamos necesarios
        title="Documentación de API",
        default_version='v1',
        description="Prueba de endpoint para API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    # No vamos a utilizar los permisos de momento para esta librería
    # permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_posts.urls)),

    # Rutas que drf_yasg va a utilizar. Modificamos algunos parámetros de la configuración por defecto que ofrece la documentación de drf_yasg
    # path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'), no la utilizamos
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```

Para consultar las páginas con la documentación que se genera de forma automática tenemos que dirigirnos a la ip de la página al path `/docs/` o `/redocs/`.

# User override

## Que es override

Un usuario de Django puede ser un super usuario, que es el que tiene permisos sobre todo el proyecto o un usuario logueado, que tiene los permisos que nosotros indiquemos que puede tener. En ambos casos, en Django, los modelos de usuario tienen una serie de atributos, como nombre, apellido, email, usuario de login, contraseña, etc. Todos estos atributos vienen predefinidos por Django. Si queremos agregar más atributos a alguno de los tipos de usuario, por ejemplo redes sociales, tenemos que hacer un override del usuario. Es una buena práctica, al comenzar un proyecto, hacer un override del usuario, aunque no agreguemos ningún atributo, que el mismo quede en blanco. Hacerlo al comienzo del proyecto va a ayudar si en un futuro queremos hacer esto mismo con el proyecto ya avanzado. Al hacer el override para los usuarios, la tabla en la base de datos que almacena lo mismo se borra y se crea una nueva tabla.

## Creando el override

Creamos una nueva app para los usuarios mediante el siguiente comando. En esta nueva app vamos a controlar a los usuario, el modelo, las vistas, los endpoint etc.

```shellscript
python manage.py startapp users
```

Editamos el archivo `models.py` de la app users que creamos para controlar los usuarios. En el mismo ingresamos el siguiente código. En el mismo heredamos el modelo por defecto de usuario de `Django` en la clase que creamos como modelo para nuestros usuarios, que en este caso es `User`. En esta primera etapa no vamos a agregar atributos al modelo de usuario, solo lo creamos. Con `pass` indicamos que termina la definición de la clase y la misma queda vacía

```py3
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Con `pass` indicamos que termina la definición de la clase y la misma queda vacía
    pass
```

Sumamos la app users para el control de los usuarios a las apps instaladas en el archivo `settings.py` de la app principal `my_blo`. 

```py3
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'rest_framework',
    'users',
    'posts',
]
```

Para indicar a nuestro proyecto que el modelo de usuario que vamos a utilizar es el que configuramos en la nueva app users, en el mismo archivo `settings.py`, al fina agregamos la siguiente línea.

```py3
STATIC_URL = 'static/'
STATIC_ROOT = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Indicamos cual es el modelo de usuario que vamos a utilizar en el proyecto
AUTH_USER_MODEL = 'user/User'
```

Confirmamos los cambios en la base de datos mediante el siguiente comando. Esto configura el proyecto para trabajar con los modelos que indicamos.

```shellscript
python manage.py makemigrations
```

Luego tenemos que ejecutar el siguiente comando para que se generen las tablas en la base de datos.

```shellscript
python manage.py migrate
```

Es posible que aparezca un error al realizar `migrate`. La mejor forma de solucionar el error es borrar todos los archivos numerados generados en las carpetas migrate, de cada una de las apps del proyecto, luego volvemos a ejecutar ambos comandos. Esta acción vuelve a configurar los modelos que armamos en la base de datos y borra todos los elementos en la misma.

Nos vemos en la necesidad de crear un nuevo superuser con el siguiente comando.

```shellscript
python manage.py createsuperuser
```

## Añadimos la app users al panel de administración

Para poder administrar los usuarios, ahora que el modelo lo manejamos nosotros desde nuestra app users, en el admin de Django, tenemos que configurar esta app para que se vea en el mismo. Para hacerlo, dentro de la carpeta de nuestra app users editamos el archivo `admin.py` con el siguiente código. Una vez terminado, cuando vayamos al panel de administración van a aparecer un nuevo panel para la app Users donde vamos a poder editar los usuarios.

```py3
# realizamos las importaciones que necesitamos
from django.contrib import admin

# el nombre de la importación UserAdmin es el mismo de la clase que creamos. En este caso podemos crear una clase con otro nombre o renombrar la importación para que no coincida. Para renombrar la importación utilizamos la palabra reservada as y el nombre que va a tomar
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from users.models import User

# utilizamos el decorador @admin.register y le pasamos el modelo user
@admin.register(User)

# Si no queremos añadir nada al panel de administración para los usuarios dejamos la clase vacía con pass
class UserAdmin(BaseUserAdmin)
    pass

```

Podemos modificar la vista del usuario, es decir, el orden de los datos que aparecen por defecto, quitando o agregando datos a esta pantalla. Para hacerlo editamos los atributos que hereda nuestra clase `AdminUser` de la clase `AdminUser` de Django. Los fieldsets son los campos de datos que se muestran en el administrador. El primer fieldset que vemos cuando abrimos el módulo de users por defecto dice 'Change user' y a continuación muestra username y password. Podemos editar todo esto o indicar que no aparezca. También podemos editar el orden de los fieldset que configuramos y que va a mostrar cada uno.

```py3
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

@admin.register(User)

class UserAdmin(BaseUserAdmin)
    fieldsets = (
        # el primer elemento de la tupla corresponde al título del fieldset, al dejarlo en None el mismo no tiene título. El segundo elemento es un diccionario donde, al la clave fields le pasamos nuevamente una tupla de valores, estos valores corresponden al modelo BaseUserAdmin. Básicamente estamos indicando con esto que datos van a aparecer en la vista para ese fieldset que dejamos sin nombre. Los datos que van a aparecer son username y password
        (None, {'fields': ('username', 'password')}),

        # Si muevo este elemento de la tupla (lo que está entre paréntesis) arriba del anterior elemento, el fieldset Información personal se va a mostrar antes que el que no tiene título
        ('Información personal', {'fields': ('first_name', 'last_name', 'email')}),
    )
```

Podemos conocer los nombres de los fields inspeccionando el código de la página por defecto y, buscando el elemento HTML donde está el campo que queremos saber el nombre, vamos a verlo en el atributo name del elemento HTML.

## Añadimos atributos a la class AdminUser personalizada

Para agregar atributos al modelo del usuario editamos el mismo en el archivo `models.py` de la app users. Agregamos aquí los atributos nuevos. Luego de actualizar el modelo de users tenemos que hacer un makemigrations y migrate.

```py3
# Importamos los modelos de datos para la base de datos
from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Creamos el atributo web_site e indicamos el tipo en la base de datos. Con black=True indicamos que el atributo puede estar vacío
    web_site = models.CharField(max_length=255, blank=True)

    twitter = models.CharField(max_length=255, blank=True)
```

Para que el nuevo campo aparezca tenemos que sumarlo como un field en las vistas personalizadas que configuramos en admin.py.

```py3
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

@admin.register(User)

class UserAdmin(BaseUserAdmin)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),       
        ('Información personal', {'fields': ('first_name', 'last_name', 'email', 'web_site')}),

        # sumamos el atributo web_site a un nuevo fieldset que llamamos Redes sociales
        ('Redes sociales', {'fields': ('web_site', 'twitter')}),
    )
```

## Cambiar el identificador username por email
