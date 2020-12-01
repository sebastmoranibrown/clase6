from django.db import models

# Create your models here.

class item(models.Model):
    title = models.CharField(max_length=50)
    detail = models.CharField(max_length=150, default="Sin descripcion")
    date_create = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
