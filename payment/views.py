from django.contrib.auth import get_user_model
from django.views import generic
from payment.models import Vendor, Product, Transaction, UserCard
from payment.forms import ContactForm, CommentForm, CardForm, CustomUserCreationForm
from django.core.mail import send_mail
from django.http import Http404
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


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
            post_data["product"] = self.get_product().id
            post_data["author"] = self.request.user.id
            kwargs["data"] = post_data
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_product()
        context["object"] = product
        context["user"] = self.request.user
        context["comments"] = product.comment_set.all()
        return context


class ProductListView(generic.ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = context["object_list"]
        context["products"] = products
        return context


class LoginCreateView(LoginRequiredMixin, generic.CreateView):
    pass


class UserDetailView(generic.DetailView):
    model = get_user_model()
    template_name = "payment/user_detail.html"
    slug_url_kwarg = "profile_slug"

    def get_slug_field(self):
        return 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transactions = context["object"].card.transaction_set.all()
        context["transactions"] = transactions
        return context


class ContactFormView(generic.FormView):
    form_class = ContactForm
    template_name = "payment/contact.html"
    success_url = "."

    def form_valid(self, form):
        data = form.cleaned_data
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


class CardFormView(generic.FormView):
    form_class = CardForm
    template_name = "payment/card.html"
    success_url = "."

    def get_initial(self):
        if(self.request.user.is_authenticated):
            return {"user_card": self.request.user.card}

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FaqView(generic.TemplateView):
    template_name = "payment/faq.html"


class RegistrationView(generic.FormView):
    form_class = CustomUserCreationForm
    template_name = "payment/signup.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
