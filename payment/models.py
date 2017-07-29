from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True)
    price = models.FloatField(blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    product_home = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=False)

    def __str__(self):
        return "{name}".format(name=self.name)

    class Meta:
        get_latest_by = "name"
        unique_together = ("name", "brand")


def uuid_generator8():
    code = uuid.uuid4().hex
    return code[:8]


class PrepaidCard(models.Model):
    barcode = models.CharField(max_length=8, default=uuid_generator8, unique=True)
    value = models.PositiveIntegerField()

    def __str__(self):
        return "{barcode}".format(barcode=self.barcode)


def uuid_generator16():
    code = uuid.uuid4().hex
    return code[:16]


class UserCard(models.Model):
    card_number = models.CharField(max_length=16, default=uuid_generator16, unique=True)
    balance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{card_number}".format(card_number=self.card_number)


class Vendor(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return "{location}".format(location=self.location)


class Inventory(models.Model):
    vendor = models.ForeignKey(Vendor)
    product = models.ForeignKey(Product)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "{vendor} -> {product} #{count}".format(vendor=self.vendor, product=self.product, count=self.count)


class Comment(models.Model):
    created = models.DateTimeField(default=datetime.datetime.now)
    message = models.TextField()
    product = models.ForeignKey(Product)
    # author field will be added

    def __str__(self):
        return "{message} ".format(message=self.message)


@receiver(pre_save, sender=Product)
def generate_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        if hasattr(sender, "name"):
            instance.slug = slugify(instance.name)
        else:
            raise AttributeError("Name field is required for slug.")
    return instance


class ExtendedUser(AbstractUser):
    card = models.OneToOneField(UserCard, null=True)
