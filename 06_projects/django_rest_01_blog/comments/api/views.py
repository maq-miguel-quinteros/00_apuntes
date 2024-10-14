from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from comments.api.serializers import CommentSerializer
from comments.api.permissions import IsOwnerOrReadAndCreateOnly
from comments.models import Comment


class CommentModelViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    # agregamos como segunda forma de filtro DjangoFilterBackend
    filter_backend = [OrderingFilter, DjangoFilterBackend]
    # mediante el - indicamos que ordene por fecha de creación pero de mayor a menor
    ordering = ['-created_at']
    filterset_fields = ['post']