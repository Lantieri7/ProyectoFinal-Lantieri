from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.email}"

class Bandas(models.Model):
    nombre=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre}"

class Vocalista(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"

class Guitarrista(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} - {self.apellido}"
    
class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatars")
    user=models.ForeignKey(User, on_delete=models.CASCADE)