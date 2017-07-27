from django.contrib import admin
from payment.models import Product

#Product
#UserCard
#PrepaidCard
#Vendor

@admin.register(Product)
class ProductAdmin (admin.ModelAdmin):
    pass

