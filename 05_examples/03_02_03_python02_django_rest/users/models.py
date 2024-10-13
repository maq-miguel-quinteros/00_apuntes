from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Tenemos que indicar que el campo email en la tabla users de la base de datos va a ser único, es decir, no se va a repetir
    email = models.EmailField(unique=True)
    web_site = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)

    # Indicamos que el nombre de usuario ahora es el registro email en la base de datos de usuario
    USERNAME_FIELD = 'email'

    # De momento no indicamos que un dato en particular es requerido
    REQUIRED_FIELDS = []