# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.viewsets import ViewSet

from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.permissions import IsAdminOrReadOnly

class PostModelViewSet(ModelViewSet):
    permission_class=[IsAdminOrReadOnly]
    serializer_class=PostSerializer
    queryset = Post.objects.all()


# class PostViewSet(ViewSet):
#     def list(self, request):
#         posts = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=posts.data)
    
#     def create(self, request):
#         post = PostSerializer(data=request.POST)
#         post.is_valid(raise_exception=True)
#         post.save()
#         return Response(status=status.HTTP_200_OK, data=post.data)
    
#     def retrieve(self, request, pk:int):
#         post = PostSerializer(Post.objects.get(pk=pk))
#         return Response(status=status.HTTP_200_OK, data=post.data)
    
# class PostApiView(APIView):
#     def get(self, request):
#         # posts_titles = [post.title for post in Post.objects.all()]
#         posts = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=posts.data)
    
#     def post(self, request):
#         # Post.objects.create(
#         #     title=request.POST['title'],
#         #     description=request.POST['description'],
#         #     order=request.POST['order']
#         # )
#         post = PostSerializer(data=request.POST)
#         post.is_valid(raise_exception=False)
#         post.save()
#         return Response(status=status.HTTP_200_OK, data=post.data)