from django.db import models

from .patient_info import PatientInformation
# PRESCRIPTION PARTS MODELS

class Prescription(models.Model):
    patient = models.ForeignKey(PatientInformation, on_delete = models.CASCADE, verbose_name = "Patient", related_name="patient_prescription")
    date_created = models.DateTimeField(auto_now_add = True)
    drug_name = models.CharField(max_length = 100, verbose_name='Drug Name')
    dosage = models.IntegerField(verbose_name = "Dosage")
    route = models.CharField(max_length=100, verbose_name="Route Taken")
    frequency = models.CharField(max_length=255, verbose_name  =  "Frequency")
    amount_dispensed = models.IntegerField(verbose_name="Amount Dispensed")
    no_of_refills = models.IntegerField(verbose_name = 'No of Refills')
    expiration_date = models.DateField(auto_now_add = False)
    notes = models.TextField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.drug_name

    class Meta:
        db_table = 'prescription'
