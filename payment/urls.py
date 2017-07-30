from django.conf.urls import url
from payment import views
from payment.views import ContactFormView, CardFormView, TransactionListView, FaqView

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^vendor/(?P<id>\d+)/$', views.VendorView.as_view(), name="vendor"),
    url(r'^product/(?P<product_slug>[\w-]+)/$', views.ProductView.as_view(), name="product"),
    url(r'^products/$', views.ProductListView.as_view(), name="products"),
    url(r'^contact/$', ContactFormView.as_view(), name="contact"),
    url(r'^card/$', CardFormView.as_view(), name='card'),
    url(r'^transactions/$', TransactionListView.as_view(), name='transactions'),
    url(r'^faq/$', FaqView.as_view(), name='faq')
]
