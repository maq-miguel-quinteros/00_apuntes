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

Al hacerlo nos va a indicar que generó una cantidad de archivos static y va a crear una carpeta en la raíz del proyecto llamada static.

Después de esto tenemos que ir al archivo `urls.py` de la app principal de nuestro proyecto. Configuramos el siguiente código.

```py3
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
