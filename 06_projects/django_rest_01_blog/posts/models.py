from django.db import models
from django.db.models import SET_NULL

from users.models import User
from categories.models import Category

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    miniature = models.ImageField(upload_to='posts/img')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    # identifica al usuario que crea el post mediante su modelo
    # con on_delete=SET_NULL() si se elimina el usuario que crea el post, el post no se va a borrar
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.title