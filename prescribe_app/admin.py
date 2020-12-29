from django.contrib import admin

from .models import Prescription, PatientInformation

admin.site.register(Prescription)
admin.site.register(PatientInformation)
