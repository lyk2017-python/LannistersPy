from django.shortcuts import render
from django.views import generic
<<<<<<< HEAD

# Create your views here.

class IndexView(generic.ListView):
    def get_queryset(self):
        return Vendor.objects.all()
=======
# Create your views here.
class HomepageView(generic.ListView):
    model =
>>>>>>> 2013cc30774588e3e35ec70c245d58138d54cf95
