from django.db import models

# Create your models here.

class List(models.Model):
    title = models.CharField(max_length=120)
    date_create = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

class Item(models.Model):
    title = models.CharField(max_length=50)
    detail = models.CharField(max_length=200)
    checked = models.BooleanField(default=False)
    date_create = models.DateField(auto_now=True)
    date_exp = models.DateField()
    list_father = models.ForeignKey(List, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

