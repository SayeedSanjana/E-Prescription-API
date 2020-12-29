from rest_framework import serializers

from prescribe_app.models import Prescription, PatientInformation
import datetime

class PrescriptionSerializerView(serializers.ModelSerializer):
    expiration_date = serializers.DateField(format="%Y-%m-%d")
    date_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    active = Prescription.objects.filter(active="False")
    # patient = PatientInformationSerializer()  
    class Meta:
        model = Prescription
        fields = ['id','drug_name' , 'dosage' , 'route', 'frequency', 'amount_dispensed', 'no_of_refills', 'expiration_date','date_created', 'active', 'notes']
    
class PrescriptionSerializerPostView(serializers.ModelSerializer):
    
    class Meta:
        model = Prescription
        fields = ['patient','drug_name' , 'dosage' , 'route', 'frequency', 'amount_dispensed', 'no_of_refills', 'expiration_date', 'active', 'notes']

    

class PrescriptionSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ['active']


