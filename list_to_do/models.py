from django.db import models

# Create your models here.

class Item(models.Model):
    """ La diferencia importante entre el definir un form y modelo, es que este max_length en el primero 
    se traduce como un atributode un input en el html. Mientras que en el segundo se traduce en un atributo
    de la base de datos. """

    title = models.CharField(max_length=50)
    datail = models.CharField(max_length=200)
    #date_expire = models.dateField()


