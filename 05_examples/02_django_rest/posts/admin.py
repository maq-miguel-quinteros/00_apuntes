# Permite agregar en admin lo que indiquemos mas abajo
from django.contrib import admin

# Traemos el modelo Post desde posts.models
from posts.models import Post

# Registramos en admin el modelo Post
@admin.register(Post)

# Creamos una clase para controlar lo que se va a ver de Post en el Admin
class PostAdmin(admin.ModelAdmin):

    # Indicamos que se muestre, de los datos de la base de datos, el título del post y la fecha de creación
    list_display = ['title', 'create_at']
