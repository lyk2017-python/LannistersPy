from django.conf.urls import url
from payment import views
from payment.views import ContactFormView, CardFormView, FaqView, RegistrationView

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^vendor/(?P<id>\d+)/$', views.VendorView.as_view(), name="vendor"),
    url(r'^product/(?P<product_slug>[\w-]+)/$', views.ProductView.as_view(), name="product"),
    url(r'^products/$', views.ProductListView.as_view(), name="products"),
    url(r'^contact/$', ContactFormView.as_view(), name="contact"),
    url(r'^card/$', CardFormView.as_view(), name='card'),
    url(r'^faq/$', FaqView.as_view(), name='faq'),
    url(r'^signup/$', RegistrationView.as_view(), name='signup'),
    url(r'^profile/(?P<profile_slug>[\w-]+)/$', views.UserDetailView.as_view(), name="profile"),
    url(r'^generator/$', views.PrepaidCardCreateView.as_view(), name="generator"),
    url(r'^generate/$', views.generate_prepaid_card, name="generate"),
    url(r'^cards/$', views.PrepaidCardListView.as_view(), name="cards")
]
