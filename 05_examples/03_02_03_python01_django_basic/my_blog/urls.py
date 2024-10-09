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
from django.urls import path

# Importamos la vista que creamos en la app posts
from posts.views import HelloWord

from posts.api

urlpatterns = [
    path('admin/', admin.site.urls),

    # Configuramos un nuevo path, en este caso cuando está vacío y le indicamos que renderice la clase HelloWord como una vista con as_view()
    path('', HelloWord.as_view()),

    # También podemos indicar una ruta específica para esa app
    path('posts/', HelloWord.as_view()),
]
