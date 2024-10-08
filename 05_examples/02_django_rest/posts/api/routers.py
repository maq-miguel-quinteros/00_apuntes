# Traemos la clase DefaultRouter que utilizamos para definir las rutas
from rest_framework.routers import DefaultRouter

# Traemos la clase PostViewSet, que creamos en las vistas
# from posts.api.views import PostViewSet

# Traemos la clase PostModelViewSet, que creamos en las vistas
from posts.api.views import PostModelViewSet

# creamos un objeto de la clase DefaultRouter
router_posts = DefaultRouter()

# mediante el método register registramos la ruta /posts/
router_posts.register(prefix='posts', basename='posts', viewset=PostModelViewSet)
