from django.contrib import admin
from web.models import Patient, Medic, Hospital

# Register your models here.
#admin.site.register(Patient)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['pfirst_name', 'plast_name', 'gender', 'age', 'medic']

@admin.register(Medic)
class MedicAdmin(admin.ModelAdmin):
    list_display = ['mfirst_name', 'mlast_name', 'expertise']
    

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ['hosname', ]
    
    

    
