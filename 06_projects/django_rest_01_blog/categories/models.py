from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    # la URL de la categoría
    slug = models.SlugField(max_length=255, unique=True)
    published = models.BooleanField(default=False)

    # para configurar un desplegable con las categorías
    def __str__(self, ):
        return self.title
