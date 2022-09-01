from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def list_patients(request):
    all_patients = models.patient.objects.all()
    context = {'patients':all_patients}
                    # |_____________________________This is something really important-- Learn what this is>>
    
    return render(request, 'office_app/lists.html', context = context)
