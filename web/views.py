from web.models import Medic, Patient
from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def patient(request):
    context = {}
    context ['patients'] = Patient.objects.all()
    return render(request, 'patient.html')

def medic(request):
    context = {}
    context ['medics'] = Medic.objects.all()
    return render(request, 'medic.html')

def hospital(request):
    return render(request, 'hospital.html')