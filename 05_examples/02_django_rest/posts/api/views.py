# Importamos los estados para las respuestas 
from rest_framework import status

# APIView tiene los diferentes métodos que vamos a utilizar como GET POST PUT que son las peticiones HTTP
from rest_framework.views import APIView

# Utilizamos Response para poder generar respuestas a las peticiones HTTP
from rest_framework.response import Response

# Traemos el modelo
from posts.models import Post

class PostApiView(APIView):
    # Redefinimos el método get de APIView para crear nuestra respuesta a una petición GET HTTP
    def get(self, request):

    # Mediante el método objects.all() de la clase (modelo) Post obtenemos todos los objetos o registros de la base de datos que se crearon en base a ese modelo
    # posts = Post.objects.all()

    # Generamos una lista (array) con todos los títulos de los post creados en la base de datos
        posts_title = [post.title for post in Post.objects.all()]

        return Response(status=status.HTTP_200_OK, data=posts_title)
    
    def post(self, request):

        # Creamos un nuevo objeto del modelo (clase) Post y le indicamos que sus datos van a ser los que vienen por la petición HTTP POST
        Post.object.crate(
            title=request.POST['title'],
            description=request.POST['description'],
            order=request.POST['order']
        )

        # Mostramos en la respuesta los datos que vinieron por POST y están en request
        return self.get(request)