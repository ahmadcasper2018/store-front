from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    decription = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)

    def __str__(self):
        return self.title
