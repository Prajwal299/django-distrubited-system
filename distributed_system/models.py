from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        app_label = 'distributed_system'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    class Meta:
        app_label = 'distributed_system'

class Order(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        app_label = 'distributed_system'
