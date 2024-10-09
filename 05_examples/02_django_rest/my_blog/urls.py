"""
URL configuration for my_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

# Traemos la clse include además de path
from django.urls import path, include
# from posts.api.views import PostApiView

# Traemos las rutas que creamos en routers.py
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
    # path('api/posts/', PostViewSet.as_view()),

    # para la ruta api/ vamos a incluir todo las rutas configuradas en el atributo urls que se crean en el objeto que este configurado en el router_posts 
    path('api/', include(router_posts.urls)),

    # Rutas que drf_yasg va a utilizar. Modificamos algunos parámetros de la configuración por defecto que ofrece la documentación de drf_yasg
    # path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'), no la utilizamos
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
