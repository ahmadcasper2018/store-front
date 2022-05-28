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
    class MEMBERSHIPS(models.TextChoices):
        GOLD = 'GOLD', 'Gold'
        SILVER = 'SILVER', 'Silver'
        BRONZ = 'BRONZ', 'Bronz'

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=30, choices=MEMBERSHIPS.choices, default=MEMBERSHIPS.BRONZ)

    def __str__(self):
        return f"customer: {self.first_name} {self.last_name}"


class Order(models.Model):
    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'

    PAYMENT_STATUS = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (FAILED, 'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=30, choices=PAYMENT_STATUS, default=PENDING)
