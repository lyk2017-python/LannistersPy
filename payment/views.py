from django.views import generic
from payment.models import Vendor, Product
from payment.forms import ContactForm,CommentForm
from django.core.mail import send_mail
from django.http import Http404

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


class ProductView(generic.CreateView):
    form_class = CommentForm
    template_name = "payment/comment_create.html"
    success_url = "."

    def get_product(self):
        query = Product.objects.filter(slug=self.kwargs["product_slug"])
        if query.exists():
            return query.get()
        else:
            raise Http404("Product not found")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.method in ["POST", "PUT"]:
            post_data = kwargs["data"].copy()
            post_data["product"] = self.get_product()
            kwargs["data"] = post_data
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object"] = self.get_product()
        return context


class ProductListView(generic.ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context["object_list"]
        context["products"] = products
        return context


class ContactFormView(generic.FormView):
    form_class = ContactForm
    template_name = "payment/contact.html"
    success_url = "."

    def form_valid(self, form):
        data = form.cleaned_data
        from django.conf import settings
        send_mail(
            "Contact Form: {}".format(data["title"]),
            ("You Have 1 New Notification\n"
             "***************\n"
             "{}\n"
             "***************\n"
             "From : {}\n"
             "IP : {}").format(data["body"], data["email"], self.request.META["REMOTE_ADDR"]),
            settings.DEFAULT_FROM_EMAIL, ["info@lannisterspy.com"])

        return super().form_valid(form)

