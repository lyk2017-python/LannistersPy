from django.conf.urls import url
from payment import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^vendor/(?P<vendor_id>\d+)/$')
]