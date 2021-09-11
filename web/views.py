from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def patient(request):
    return render(request, 'patient.html')

def medic(request):
    return render(request, 'medic.html')

def hospital(request):
    return render(request, 'hospital.html')