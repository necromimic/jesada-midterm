from django.urls import path
from web.views import index, patient, medic, hospital
urlpatterns = [
    path('' , index, name='index'),
    path('patient/' , patient, name='patient'),
    path('medic/' , medic, name='medic'),
    path('hospital/' , hospital, name='hospital'),
]