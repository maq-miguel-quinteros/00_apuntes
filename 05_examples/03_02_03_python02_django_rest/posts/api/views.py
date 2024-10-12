from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.permissions import IsAdminOrReadOnly

class PostModelViewSet(ModelViewSet):
    permission_class = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()