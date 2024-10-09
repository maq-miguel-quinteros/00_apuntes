# Importamos models, que nos permite crear los modelos
from django.db import models

class Post(models.Model):
    # Los atributos de la clase Post van a ser del tipo de las clases en models
    title = models.CharField(max_length=255)
    description = models.TextField()

    # Mediante auto_created=True indicamos que, al crearse un nuevo registro, la fecha se crea de forma automática con el valor de la fecha de ese momento
    created_at = models.DateTimeField(auto_created=True)

    # Agregamos este atributo después de haber creado la tabla en la base de datos mediante makemigrations y migrate
    order = models.IntegerField()