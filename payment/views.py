from django.views import generic
from payment.models import Vendor, Product


class IndexView(generic.ListView):
    model = Vendor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vendors = context["object_list"]
        for vendor in vendors:
            inventories = vendor.inventory_set.all()
            vendor.product_names = [inventory.product.name for inventory in inventories]
            vendor.stock_count = 0
            for inventory in inventories:
                vendor.stock_count += inventory.count

        context["vendors"] = vendors
        return context


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


class ProductListView(generic.ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context["object_list"]
        context["products"] = products
        return context


