# Importamos los estados para las respuestas 
from rest_framework import status

# APIView tiene los diferentes métodos que vamos a utilizar como GET POST PUT que son las peticiones HTTP
from rest_framework.views import APIView

# Importamos ViewSet
from rest_framework.viewset import ViewSet

# Utilizamos Response para poder generar respuestas a las peticiones HTTP
from rest_framework.response import Response

# Traemos el modelo
from posts.models import Post

# Traemos el serializador que creamos en serializers.py
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