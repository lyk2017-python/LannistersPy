from django.contrib import admin
from payment.models import Product,UserCard, PrepaidCard, Vendor

#Product
#UserCard
#PrepaidCard
#Vendor

@admin.register(Product)
class ProductAdmin (admin.ModelAdmin):
    list_display = [
        "name",
        "brand",
        "price",
    ]
    search_fields = [
        "name",
        "brand",
        "price",
    ]
@admin.register(UserCard)
class UserCardAdmin (admin.ModelAdmin):
    pass

@admin.register(PrepaidCard)
class PrepaidCardAdmin (admin.ModelAdmin):
    pass

@admin.register(Vendor)
class VendorAdmin (admin.ModelAdmin):
    pass


