from django.db import models

class Collection(models.Model):
    titile = models.CharField(max_length=225)


class Product(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    title = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now_add=True)


class Customer(models.model):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12)
    birth_date = models.DateField(null=True)

    
