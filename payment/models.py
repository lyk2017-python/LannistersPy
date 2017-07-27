
from django.db import models
import uuid


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    price = models.FloatField()
    brand = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    product_home = models.URLField()
    count = models.PositiveIntegerField()
    slug = models.SlugField()

    def __str__(self):
        return "{name}".format(name=self.name)
    # Model options

    class Meta:
        get_latest_by = "name"
        unique_together = ("name", "brand")


def uuidGenerator8():
    code = uuid.uuid4().hex
    return code[:8]


class PrepaidCard(models.Model):
    barcode = models.CharField(max_length=8, default=uuidGenerator8, unique=True)
    value = models.PositiveIntegerField()

    def __str__(self):
        return "{barcode}".format(barcode=self.barcode)


def uuidGenerator16():
    code = uuid.uuid4().hex
    return code[:16]


class UserCard(models.Model):
    card_number = models.CharField(max_length=16, default=uuidGenerator16, unique=True)
    balance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{card_number}".format(card_number=self.card_number)


class Vendor(models.Model):
    location = models.CharField(max_length=50)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return "{location}".format(location=self.location)
