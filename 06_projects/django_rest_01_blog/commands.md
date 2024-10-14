# Nuevo proyecto

`consola`

```shellscript
python -m venv venvs/blog
venvs/blog/Scripts/activate
pip3 install django
django-admin startproject blog .
python manage.py runserver
```

# Override de usuario

```shellscript
python manage.py startapp users
```

`settings.py` de `blog`

```py3
INSTALLED_APPS = [
	...
    'users',
]
```

`models.py` de `users`

```py3
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

`admin.py` de `users`

```py3
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User

@admin.register(User)

class UserAdmin(BaseUserAdmin):
    pass
```

`settings.py` de `blog`

```py3
...
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'
```

`consola`

```shellscript
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

`models.py` de `users`

```py3
class User(AbstractUser):
    email = models.EmailField(unique=True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS= []
```

# Instalando djangorest

`consola`

```shellscript
pip3 install djangorestframework
```

`settings.py` de `blog`

```py3
INSTALLED_APPS = [
	...
	'django.contrib.staticfiles',
    'rest_framework',
    'users',
]
```

# Documentación de la API con drf-yasg

`consola`

```shellscript
pip3 install -U drf-yasg
```

`settings.py` de `blog`

```py3
INSTALLED_APPS = [
	...
    'rest_framework',
	'drf_yasg',
    'users',
]
```

`urls.py` de `blog`

```py3
# drf-yasg
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# drf-yasg
schema_view = get_schema_view(
	openapi.Info(
		title="Blog API",
		default_version='v1',
		description="Documentación de la API de blog",
		terms_of_service="",
		contact=openapi.Contact(email="admi@admin.com"),
		license=openapi.License(name="BSD License"),	
    ),
	public=True,
	permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # drf-yasg
    # path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
	path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```

`settings.py` de `blog`

```py3
...
STATIC_URL = 'static/'
STATIC_ROOT = './static/'
...
```

`consola`

```shellscript
python manage.py collectstatic
pip3 install setuptools # por error con drf-yasg
python manage.py runserver
```

# Registro de usuarios

1. Nueva carpeta `api` en `users`

2. Nuevo archivo en `api`, de `users`, llamado `__init__.py`
3. Nuevo archivo en `api`, de `users`, llamado `views.py`
4. Nuevo archivo en `api`, de `users`, llamado `serializers.py`
5. Nuevo archivo en `api`, de `users`, llamado `routers.py`

`views.py` de `api` en `users`

```py3
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User

class RegisterView(APIView):
    def post(self, request):
        print('registrando usuario...')
        return Response(status=status.HTTP_400_BAD_REQUEST)
```

`routers.py` de `api` en `users`

```py3
from django.urls import path
from users.api.views import RegisterView

urlpatterns = [
    path('auth/register', RegisterView.as_view()),
]
```

`urls.py` de `blog`

```py3
...
from django.urls import path, include
...
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include('users.api.routers'))
	...
]
```

# Lógica para registrar los usuarios

`serializers.py` de `api` en `users`

```py3
from rest_framework import serializers
from users.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']
```

`views.py` de `api` en `users`

```py3
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.api.serializers import UserRegisterSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

# Encriptando contraseña

`serializers.py` de `api` en `users`

```py3
	...
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        
        return instance
```

# Login con JWT

`consola`

```shellscript
pip3 install djangorestframework-simplejwt
```

`settings.py` de `blog`

```py3
...
AUTH_USER_MODEL = 'users.User'

# JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
```

`routers.py` de `api` en `users`

```py3
from django.urls import path
from users.api.views import RegisterView

# JWT
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('auth/register', RegisterView.as_view()),

    # JWT
    path('auth/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

# Obtener los datos del usuario logueado

`serializers.py` de `api` en `users`

```py3
...
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name']
```

`views.py` de `api` en `users`

```py3
...
from rest_framework.permissions import IsAuthenticated
from users.api.serializers import UserRegisterSerializer
from users.api.serializers import UserSerializer
...
class UserView(APIView):
    permission_class = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, )
```

`routers.py` de `api` en `users`

```py3
...
from users.api.views import UserView
...
urlpatterns = [
    path('auth/register', RegisterView.as_view()),
    path('auth/me', UserView.as_view()),
	...
]
```

# Actualizando datos de usuario

`serializers.py` de `api` en `users`

```py3
...
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
```

`views.py` de `api` en `users`

```py3
...
from users.api.serializers import UserUpdateSerializer
from users.models import User
...
class UserView(APIView):
    ...
	def put(self, request):        
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

# Modelo para categorías

`consola`

```shellscript
python manage.py startapp categories
```

`settings.py` de `blog`

```py3
INSTALLED_APPS = [
	...
    'users',
    'categories',
]
```

`models.py` de `categories`

```py3
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    # la URL de la categoría
    slug = models.SlugField(max_length=255, unique=True)
    published = models.BooleanField(default=False)

    # para configurar un desplegable con las categorías
    def __str__(self, ):
        return self.title
```

`consola`

```shellscript
python manage.py makemigrations
python manage.py migrate
```

`admin.py` de `categories`

```py3
from django.contrib import admin
from categories.models import Category

@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'published']
```

# CRUD para categories

1. Nueva carpeta `api` en `categories`

2. Nuevo archivo en `api`, de `categories`, llamado `__init__.py`
3. Nuevo archivo en `api`, de `categories`, llamado `views.py`
4. Nuevo archivo en `api`, de `categories`, llamado `serializers.py`
5. Nuevo archivo en `api`, de `categories`, llamado `routers.py`

`serializers.py` de `api` en `categories`

```py3
from rest_framework import serializers
from categories.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'slug', 'published']
```

`views.py` de `api` en `categories`

```py3
from rest_framework.viewsets import ModelViewSet
from categories.api.serializers import CategorySerializer
from categories.models import Category

class CategoryApiViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
```

`routers.py` de `api` en `categories`

```py3
from rest_framework.routers import DefaultRouter
from categories.api.views import CategoryApiViewSet

router_categories = DefaultRouter()
router_categories.register(prefix='categories', basename='categories', viewset=CategoryApiViewSet)
```

`urls.py` de `blog`

```py3
...
from categories.api.routers import router_categories
...
urlpatterns = [
	...
    path('api/', include(router_categories.urls)),
    ...
]
```

`serializers.py` de `api` en `categories`

```py3
...
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # sumamos id
        fields = ['id', 'title', 'slug', 'published']
```

# Permisos a los endpoint de categories

Nuevo archivo en `api`, de `categories`, llamado `permissions.py`

```py3
from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff
```

`views.py` de `api` en `categories`

```py3
...
from categories.api.permissions import IsAdminOrReadOnly
...

class CategoryApiViewSet(ModelViewSet):
    permission_class = IsAdminOrReadOnly
	...
```

# Búsqueda de categories mediante slug

`views.py` de `api` en `categories`

```py3
...

class CategoryApiViewSet(ModelViewSet):
	...
    lookup_field = 'slug'
```

# Filtros

## Filtro en todas las peticiones HTTP

`views.py` de `api` en `categories`

```py3
...

class CategoryApiViewSet(ModelViewSet):
	...
    # queryset = Category.objects.all()
	# el filtro se aplica para cualquier petición HTTP
    queryset = Category.objects.filter(published=True)
	...
```

## Utilizando django-filter

`consola`

```shellscript
pip3 install django-filter
```

`settings.py` de `blog`

```py3

INSTALLED_APPS = [
	...
    'rest_framework',
    'django_filters',
    'drf_yasg',
	...
]
```

`views.py` de `api` en `categories`

```py3
...
from django_filters.rest_framework import DjangoFilterBackend
...

class CategoryApiViewSet(ModelViewSet):
	...
    # queryset = Category.objects.filter(published=True)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['published', 'title']
```

# app y modelo para posts

`consola`

```shellscript
python manage.py startapp posts
```

`settings.py` de `blog`

```py3
INSTALLED_APPS = [
	...
    'categories',
    'posts',
]
```

`models.py` de `posts`

```py3
from django.db import models
from django.db.models import SET_NULL

from users.models import User
from categories.models import Category

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    miniature = models.ImageField(upload_to='posts/img')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    # models.ForeignKey identifica al usuario que crea el post mediante su modelo
    # con on_delete=SET_NULL() si se elimina el usuario que crea el post, el post no se va a borrar
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)
    
	def __str__(self):
        return self.title
```

`admin.py` de `posts`

```py3
from django.contrib import admin
from posts.models import Post

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'published']
```

`consola`

```shellscript
python manage.py makemigrations
pip3 install Pillow # si makemigrations da error
python manage.py migrate

```

# CRUD para posts

1. Nueva carpeta `api` en `posts`
2. Nuevo archivo en `api`, de `posts`, llamado `__init__.py`
3. Nuevo archivo en `api`, de `posts`, llamado `views.py`
4. Nuevo archivo en `api`, de `posts`, llamado `serializers.py`
5. Nuevo archivo en `api`, de `posts`, llamado `routers.py`

`serializers.py` de `api` en `posts`

```py3
from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'miniature', 'created_at', 'published', 'user', 'category']
```

`views.py` de `api` en `posts`

```py3
from rest_framework. viewsets import ModelViewSet
from posts.models import Post
from posts.api.serializers import PostSerializer

class PostModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
```

`routers.py` de `api` en `posts`

```py3
from rest_framework.routers import DefaultRouter
from posts.api.views import PostModelViewSet

router_posts = DefaultRouter()
router_posts.register(prefix='posts', basename='posts', viewset=PostModelViewSet)
```

`urls.py` de `blog`

```py3
...
from categories.api.routers import router_categories
from posts.api.routers import router_posts
...
urlpatterns = [
	...
    path('api/', include(router_categories.urls)),
    path('api/', include(router_posts.urls)),
	...
]
```

# Permisos en los posts

Nuevo archivo en `api`, de `posts`, llamado `permissions.py`

```py3
from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff
```

`views.py` de `api` en `posts`

```py3
...
from posts.api.permissions import IsAdminOrReadOnly

class PostModelViewSet(ModelViewSet):
    permission_class = IsAdminOrReadOnly
	...
```

# Obtener información de user y category al consultar un post

`serializers.py` de `api` en `posts`

```py3
...
from users.api.serializers import UserSerializer
from categories.api.serializers import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'miniature', 'created_at', 'published', 'user', 'category']
```

# Obtener todos los post de una category

## Filtrando por id de category

`views.py` de `api` en `posts` -> _http://127.0.0.1:8000/api/posts/?category=1_

```py3
from django_filters.rest_framework import DjangoFilterBackend
...
class PostModelViewSet(ModelViewSet):
	...    
    filter_backend = [DjangoFilterBackend]
    filter_fields = ['category']
```

## Filtrando por slug de category

`views.py` de `api` en `posts` -> _http://127.0.0.1:8000/api/posts/?category__slug=react_

```py3
from django_filters.rest_framework import DjangoFilterBackend
...
class PostModelViewSet(ModelViewSet):
	...    
    filter_backend = [DjangoFilterBackend]
    # filter_fields = ['category']
    filter_fields = ['category__slug']
```

# App y modelo para comentarios

`consola`

```shellscript
python manage.py startapp comments
```

`settings.py` de `blog`

```py3
INSTALLED_APPS = [
	...
    'posts',
    'comments',
]
```

`models.py` de `comments`

```py3
from django.db import models
from django.db.models import CASCADE

from users.models import User
from posts.models import Post

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # al borrar el usuario se borran todos sus comentarios
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=CASCADE, null=True)
```

`consola`

```shellscript
python manage.py makemigrations
python manage.py migrate
```

`admin.py` de `comments`

```py3
from django.contrib import admin
from comments.models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'user', 'post', 'created_at']
```

# CRUD para comments

1. Nueva carpeta `api` en `comments`
2. Nuevo archivo en `api`, de `comments`, llamado `__init__.py`
3. Nuevo archivo en `api`, de `comments`, llamado `views.py`
4. Nuevo archivo en `api`, de `comments`, llamado `serializers.py`
5. Nuevo archivo en `api`, de `comments`, llamado `routers.py`

`serializers.py` de `api` en `comments`

```py3
from rest_framework import serializers
from comments.models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'created_at', 'user', 'post']
```

`views.py` de `api` en `comments`

```py3
from rest_framework.viewsets import ModelViewSet
from comments.api.seriealizers import CommentSerializer
from comments.models import Comment


class CommentModelViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
```

`routers.py` de `api` en `comments`

```py3
from rest_framework.routers import DefaultRouter
from comments.api.views import CommentModelViewSet

router_comments = DefaultRouter()
router_comments.register(prefix='comments', basename='comments', viewset=CommentModelViewSet)
```

`urls.py` de `blog`

```py3
...
from posts.api.routers import router_posts
from comments.api.routers import router_comments
...
urlpatterns = [
	...
    path('api/', include(router_posts.urls)),
    path('api/', include(router_comments.urls)),
	...
]
```

# Ordenar comentarios

`views.py` de `api` en `comments`

```py3
...
from rest_framework.filters import OrderingFilter
...
class CommentModelViewSet(ModelViewSet):
	...
    filter_backend = [OrderingFilter]
    # mediante el - indicamos que ordene por fecha de creación pero de mayor a menor
    ordering = ['-created_at']
```

# Obtener todos los comentarios de un post

`views.py` de `api` en `comments` -> http://127.0.0.1:8000/api/comments/?post={id}

```py3
...
from django_filters.rest_framework import DjangoFilterBackend
...
class CommentModelViewSet(ModelViewSet):
	...
    # agregamos como segunda forma de filtro DjangoFilterBackend
    filter_backend = [OrderingFilter, DjangoFilterBackend]
	...
    filterset_fields = ['post']
    
```

# Permisos para comments

Nuevo archivo en `api`, de `comments`, llamado `permissions.py`

```py3
from rest_framework.permissions import BasePermission
from comments.models import Comment

class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            # peticiones HTTP que no son ni GET ni POST (las que modifican)
            # id del comentario
            id_comment = view.kwargs['pk']
            # traemos el comentario
            comment = Comment.objects.get(pk=id_comment)
            # id del usuario que hizo ese comentario
            id_user_comment = comment.user_id

            # id del usuario que hace la petición HTTP
            id_user = request.user.pk

            # si el usuario que hace la petición de modificar o eliminar es el mismo que creó el comentario
            if id_user_comment == id_user:
                return True

            return False
```

`views.py` de `api` en `comments`

```py3
...
from comments.api.permissions import IsOwnerOrReadAndCreateOnly
from comments.models import Comment


class CommentModelViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
	...
```
