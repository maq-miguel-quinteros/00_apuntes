from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):

    # redefinimos el método has_permission que heredamos de la clase BasePermission
    def has_permission(self, request, view):

        # Si el método que tiene como atributo request es GET devuelve True, es decir, tiene permisos para realizar la petición HTTP
        if request.method == 'GET':
            return True
        else:
            # Devuelve el valor del atributo is_staff del objeto user, del objeto request. Si es un usuario administrador devuelve True, es decir, tiene permisos para realizar pa petición HTTP que esta realizando. Si el valor de is_staff es False, es decir, no es un administrador, devuelve false y no puede realizar la petición
            return request.user.is_staff