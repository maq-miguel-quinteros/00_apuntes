"""
URL configuration for blog project.

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
from django.urls import path, include

from categories.api.routers import router_categories
from posts.api.routers import router_posts
from comments.api.routers import router_comments

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
    path('api/', include('users.api.routers')),
    path('api/', include(router_categories.urls)),
    path('api/', include(router_posts.urls)),
    path('api/', include(router_comments.urls)),

    # drf-yasg
    # path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
	path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
	path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
