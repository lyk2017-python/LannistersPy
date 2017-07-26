from django.conf.urls import url
from payment import views

urlpatterns = [
    url(r'^$', views.IndexView, name="index"),
    url(r'^vendor/(?P<vendor_id>\d+)/$', views.VendorView, name="vendor"),
    url(r'^product/(?P<product_slug>\w+)\$', views.ProductView, name="product"),
]
