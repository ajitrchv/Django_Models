from django.urls import path, reverse
from django.http import HttpResponseRedirect

def home(request):
    return(HttpResponseRedirect(reverse('list_patients')))