from django.db import models


# Create your models here.
class Collection(models.Model):
    title = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    decription = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(
        Collection,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.title


class Order(models.Model):
    PENDING = 'P'
    COMPLETED = 'C'
    FAILED = 'F'

    PAYMENT_STATUS = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (FAILED, 'Failed'),
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS, default=PENDING)


class Customer(models.Model):
    GOLD = 'G'
    SILVER = 'S'
    BRONZ = 'B'

    MEMBER_CHOICES = [
        (GOLD, 'Gold'),
        (SILVER, 'Silver'),
        (BRONZ, 'Bronz'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBER_CHOICES, default=BRONZ)
    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f"customer: {self.first_name} {self.last_name}"


class Address(models.Model):
    street = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT
    )
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=3)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

