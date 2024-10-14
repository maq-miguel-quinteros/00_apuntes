from rest_framework.permissions import BasePermission
from comments.models import Comment

class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' or request.method == 'POST':
            return True
        else:
            # peticiones HTTP que no son ni GET ni POST (las que modifican)
            # id del comentario
            id_comment = view.kwargs['pk']
            # traemos el comentario
            comment = Comment.objects.get(pk=id_comment)
            # id del usuario que hizo ese comentario
            id_user_comment = comment.user_id

            # id del usuario que hace la petición HTTP
            id_user = request.user.pk

            # si el usuario que hace la petición de modificar o eliminar es el mismo que creó el comentario
            if id_user_comment == id_user:
                return True

            return False


