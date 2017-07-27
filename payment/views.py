from django.views import generic
from payment.models import Vendor, Product


class IndexView(generic.ListView):
    model = Vendor


class VendorView(generic.DetailView):
    model = Vendor
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["inventories"] = context["object"].inventory_set.all()
        return context


class ProductView(generic.DetailView):
    model = Product
    slug_url_kwarg = 'product_slug'
