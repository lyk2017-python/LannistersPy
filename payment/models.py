from django.db import models
import uuid


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    brand = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    product_home = models.URLField()
    count = models.PositiveIntegerField()


def uuidGeneratorPrepaid(self):
    code = str(uuid.uuid4())
    return code[:10]

class PrepaidCard(models.Model):
    barcode = models.CharField(max_length=8,default=uuidGeneratorPrepaid)
    value = models.PositiveIntegerField()

def uuidGeneratorUserCard(self):
    code = str(uuid.uuid4())
    return code[:18]


class UserCard(models.Model):
    card_number = models.CharField(max_length=16, default=uuidGeneratorUserCard)
    balance = models.PositiveIntegerField()


