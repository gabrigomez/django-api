from django.db import models

# Create your models here.

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    email = models.CharField(unique=True)
    password = models.CharField(max_length=100)
    language = models.TextField(max_length=20, default='')
    
