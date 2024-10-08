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


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/posts/', PostViewSet.as_view()),

    # para la ruta api/ vamos a incluir todo las rutas configuradas en el atributo urls que se crean en el objeto que este configurado en el router_posts 
    path('api/', include(router_posts.urls))
]
