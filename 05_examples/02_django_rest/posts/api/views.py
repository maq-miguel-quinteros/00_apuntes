# Importamos los estados para las respuestas 
from rest_framework import status

# APIView tiene los diferentes métodos que vamos a utilizar como GET POST PUT que son las peticiones HTTP
from rest_framework.views import APIView

# Importamos ViewSet
from rest_framework.viewset import ViewSet, ModelViewSet

# Utilizamos Response para poder generar respuestas a las peticiones HTTP
from rest_framework.response import Response

# Traemos el modelo
from posts.models import Post

# Traemos el serializador que creamos en serializers.py
from posts.api.serializers import PostSerializer

# Importamos las clases con los tipos de permisos:
# IsAuthenticated dará permisos solo a los usuarios autenticados para hacer peticiones a este modelo
# IsAdminUser si el usuario es administrador del proyecto (usuario admin que creamos)
# IsAuthenticatedOrReadOnly si no es un usuario autenticado solo puede hacer consultas de lectura 
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly

# Mediante la clase PostModelViewSet y redefiniendo el valor de los atributos que hereda de ModelViewSet creamos el CRUD completo
class PostModelViewSet(ModelViewSet):

    # Redefinimos el atributo indicando las clases con los tipos de permisos que van a tener sobre el CRUD que creamos
    permission_class = [IsAuthenticatedOrReadOnly]

    # Indicamos cual es el serializador que va a dar formato a los datos que enviamos y recibimos
    serializer_class = PostSerializer

    # Indicamos la query que va a manejar las llamadas a la base de datos, en este caso la query indica traer todos los elementos de la base de datos
    queryset = Post.objects.all()


# class PostViewSet(ViewSet):
#     # Mediante el método list traemos un listado de los post guardados en la base de datos
#     def list(self, request):
#         posts = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=posts.data)

#     # Redefinimos el método que configura la ruta /api/posts/id donde el parámetro pk que pasamos es el id del registro en la base de datos que queremos obtener. Podemos o no indicar el tipo de dato de pk
#     def retrieve(self, request, pk: int):

#         # mediante el método get indicamos traer solo el registro en la base de datos con el valor de id = al pk que pasamos por parámetro
#         post = PostSerializer(Post.objects.get(pk=pk))
        
#         return Response(status = status.HTTP_200_OK, data = post.data)

    
#     # Mediante create creamos un nuevo post en la base de datos
#     def create(self, request):
#         post = PostSerializer(data=request.POST)
#         post.is_valid(raise_exception=True)
#         post.save()
#         return Response(status=status.HTTP_200_OK, data=post.data)


# class PostApiView(APIView):
#     # Redefinimos el método get de APIView para crear nuestra respuesta a una petición GET HTTP
#     def get(self, request):

#     # Mediante el método objects.all() de la clase (modelo) Post obtenemos todos los objetos o registros de la base de datos que se crearon en base a ese modelo
#     # posts = Post.objects.all()

#     # Generamos una lista (array) con todos los títulos de los post creados en la base de datos
#         # posts_title = [post.title for post in Post.objects.all()]

#         # A la clase PostSerializer le pasamos todos los objetos (registros) de Post que vienen de la base de datos. Con many=True le indicamos que devuelva el array o lista completas de estos posts
#         post = PostSerializer(Post.objects.all(), many=True)

#         return Response(status=status.HTTP_200_OK, data=post.data)
    
#     def post(self, request):

#         # Creamos un nuevo objeto del modelo (clase) Post y le indicamos que sus datos van a ser los que vienen por la petición HTTP POST
# #       Post.objects.create(
# #             title=request.POST['title'],
# #             description=request.POST['description'],
# #             order=request.POST['order']
# #         )

# #         # Mostramos en la respuesta los datos que vinieron por POST y están en request
# #         return self.get(request)

#         # Pasamos a la clase PostSerializer los datos de la petición HTTP POST que llegan en request
#         post = PostSerializer(data=request.POST)

#         # Mediante el método is_valid validamos los datos que llegan en request. Si los datos no son validos va a generar una excepción
#         post.is_valid(raise_exception=True)

#         # Guardamos los datos en la base de datos
#         post.save()

#         return Response(status=status.HTTP_200_OK, data=post.data)