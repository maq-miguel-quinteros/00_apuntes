# Autenticación con JWT

## Instalación

Para implementar el standard de autenticación Json Web Token (JWT) instalamos la siguiente dependencia. Este permite gestionar las sesiones mediante 2 token. El access token permite entrar en la aplicación y otro token que refresca el primero aumentando la seguridad. [JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation)

```shellscript
pip3 install djangorestframework-simplejwt
```

Editamos el archivo `settings.py` de la app principal del proyecto y añadimos el siguiente código.

```py3
# Agregamos la configuración para JWT
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (        
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )    
}
```

## Rutas

En general las rutas se configuran en el archivo `urls.py` de la app principal del proyecto. Si generamos usuarios personalizados haciendo un override el ideal es configurar las rutas en la app users creada para controlar esos usuarios personalizados. Dentro de la carpeta de la app users creamos una nueva carpeta llamada api. Dentro de api creamos un nuevo archivo llamado `routers.py`.

```py3
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Le pasamos la ruta de login para el usuario. Pasamos la vista que va a tener en ese path y le damos un nombre
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # La ruta que refresca el access token indicamos la siguiente
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Las configuraciones que vienen por defecto
    # path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
]
```

Importamos las rutas que creamos en `routers.py` de la carpeta de la app users. En lugar de hacer import para traer los datos utilizamos directamente include dentro del método path como en el siguiente código.

```py3
urlpatterns = [
	...
    # include va a traer las rutas que configuramos el el router de la carpeta api de la app users 
    path('api/', include('users.api.routers')),
	...
]
```

## Tiempo de caducidad de los token

Para modificar el tiempo de caducidad de los token, editamos el archivo `settings.py` de la app principal del proyecto.

```py3
# importamos el tipo de datos que vamos a utilizar para indicar el tiempo
import datetime

...

SIMPLE_JWT = {
    # Cambiamos el tiempo de caducidad de ambos token indicando minutos y días
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=7),
}
```
