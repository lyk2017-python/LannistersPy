from django.views import generic
from payment.models import Vendor, Product

# Create your views here.


class IndexView(generic.ListView):
    model = Vendor


class VendorView(generic.DetailView):
    model = Vendor
    pk_url_kwarg = 'id'


class ProductView(generic.DetailView):
    model = Product
    slug_url_kwarg = 'product_slug'
