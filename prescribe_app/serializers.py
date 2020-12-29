# from rest_framework import serializers

# from .models import Prescription, PatientInformation

# class PatientInformationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PatientInformation
#         fields = ('id', 'l_name', 'f_name', 'age', 'bday', 'contact', 'email', 'active')

# class PatientInformationSerializerActive(serializers.ModelSerializer):
#     class Meta:
#         model = PatientInformation
#         fields = ['active']

# class PrescriptionSerializerView(serializers.ModelSerializer):
#     expiration_date = serializers.DateField(format="%Y-%m-%d")
#     date_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
#     active = Prescription.objects.filter(active="False")
#     # patient = PatientInformationSerializer()  
#     class Meta:
#         model = Prescription
#         fields = ['id','drug_name' , 'dosage' , 'route', 'frequency', 'amount_dispensed', 'no_of_refills', 'expiration_date','date_created', 'active']
    
# class PrescriptionSerializerPostView(serializers.ModelSerializer):
    
#     class Meta:
#         model = Prescription
#         fields = ['patient','drug_name' , 'dosage' , 'route', 'frequency', 'amount_dispensed', 'no_of_refills', 'expiration_date', 'active']



# class PrescriptionSerializerPost(serializers.ModelSerializer):
#     class Meta:
#         model = Prescription
#         fields = ['active']


# #######    SERIALIZER FOR DETAIL VIEW OF ALL PRESCRIPTION PER PATIENT ##########
# class PatientDetailSerializer(serializers.ModelSerializer):
#     queryset = Prescription.objects.filter(active="False")
#     patient_prescription = PrescriptionSerializerView(many=True, read_only=True)
#     class Meta:
#         model = PatientInformation
#         fields = ('id', 'l_name', 'f_name', 'age', 'bday', 'contact', 'email', 'active', 'patient_prescription')

   