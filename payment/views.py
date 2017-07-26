from django.views import generic
from payment.models import Vendor, Product

# Create your views here.


class IndexView(generic.ListView):
    model = Vendor


class VendorView(generic.ListView):
    model = Product


class ProductView(generic.DetailView):
    model = Product
    slug_url_kwarg = 'product_slug'
