from django.contrib import admin
from web.models import Patient

# Register your models here.
#admin.site.register(Patient)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['pfirst_name', 'plast_name', 'gender', 'age']
    
