from django.db import models

from .patient_info import PatientInformation

class Notes(models.Model):
    patient = models.ForeignKey(PatientInformation, on_delete=models.CASCADE, related_name='patients_notes')
    notes = models.TextField(max_length=255, verbose_name="Notes")
    date_created = models.DateTimeField(auto_now_add=True)

    def _str__(self):
        return self.patient.l_name + "," + self.patient.f_name

    class Meta:
        db_table = 'notes'