from django.conf.urls import url
from payment import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^vendor/(?P<id>\d+)/$', views.VendorView.as_view(), name="vendor"),
    url(r'^product/(?P<product_slug>[\w-]+)/$', views.ProductView.as_view(), name="product"),
]
