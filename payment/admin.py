from django.contrib import admin
from payment.models import *


class VendorInline(admin.StackedInline):
    model = Inventory
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('slug',)
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
    list_filter = [
        "name", # Filters in list screen.
        "brand",
        "price",
    ]


@admin.register(UserCard)
class UserCardAdmin(admin.ModelAdmin):
    list_display = [
        "card_number",
        "balance",
    ]
    search_fields = [
        "card_number",
        "balance",
    ]


@admin.register(PrepaidCard)
class PrepaidCardAdmin(admin.ModelAdmin):
    exclude = ('is_used',)
    list_display = [
        "barcode",
        "value",
        "is_used"
    ]
    search_fields = [
        "barcode",
        "value",
        "is_used"
    ]
    list_filter = [
        "value",
        "is_used"
    ]


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    inlines = [VendorInline]
    list_display = [
        "location",
    ]
    search_fields = [
        "location",
    ]
    list_filter = [
        "location"  # Filters in list screen.
    ]