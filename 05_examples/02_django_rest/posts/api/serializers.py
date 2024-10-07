# Importamos la clase que permite hacer la serialización
from rest_framework.serializers import ModelSerializer

from posts.models import Post

# Creamos una clase para hacer la serialización del modelo de Post
class PostSerializer(ModelSerializer):

    # Pasamos los datos correspondientes al modelo, como cual es el modelo y con fields cuales son los datos de este modelo que tiene que serializar
    class Meta:
        model = Post

        # Mediante __all__ podeos indicar que debe serializar todos los datos. La forma correcta de trabajar es indicar en una lista los datos que queremos realmente que serialice
        fields = ['title', 'description', 'order', 'create_at']
