from django.shortcuts import render
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    def get_queryset(self):
        return Vendor.objects.all()