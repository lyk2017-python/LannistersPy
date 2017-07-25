from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    brand = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    url = models.URLField()
    count = models.PositiveIntegerField()


class PrepaidCard(models.Model):
    number = models.CharField(max_length=8)
    value = models.PositiveIntegerField()


class UserCard(models.Model):
    card_number = models.CharField(max_length=16)
    balance = models.PositiveIntegerField()

