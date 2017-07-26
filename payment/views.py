from django.shortcuts import render
from django.views import generic
from payment.models import Vendor, Product

# Create your views here.

class IndexView(generic.ListView):
    def get_queryset(self):
        return Vendor.objects.all()


class VendorView(generic.ListView):
    def get_queryset(self):
        return Product.objects.all()


class ProductView(generic.DetailView):
    model = Product
