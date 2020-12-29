from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny
from prescribe_app.serializers_folder.patient_serializers import ( 
    PatientInformationSerializer, 
    PatientDetailSerializer,
    PatientInformationSerializerActive

)
from prescribe_app.models import Prescription, PatientInformation


#######    LIST API VIEW FOR SHOWING THE LIST OF ALL PRESCRIPTION AND PATIENT / POST METHOD FOR ADDING NEW PRESCRIPTION ##########
@api_view(['GET', 'POST'])
def patients_view(request):

    if request.method == 'GET':
        patient = PatientInformation.objects.all()
        serializer = PatientInformationSerializer(patient, many=True)
        
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'POST' :
        
        serializer = PatientInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Data is saving")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Error in POST Method")
            content = {'Error': 'Invalid data'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#######    DETAIL API VIEW FOR SHOWING THE LIST OF PRESCRIPTION FOR EVERY PATIENT ##########
@api_view(['GET', 'PUT', 'DELETE'])
def patient_info_detail(request, pk):
    
    if request.method == 'GET':
        patient = PatientInformation.objects.get(id=pk)
        
        serializer = PatientDetailSerializer(instance=patient)
        return Response(serializer.data)
    
    

    elif request.method == 'PUT':
        obj = PatientInformation.objects.get(id=pk)
        serializer = PatientInformationSerializerActive(instance=obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            content = {'Error': 'Invalid data'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)
    else:
        content = {
            'Error' :' Patient Information Not Found'
        }
        return Response(content,status=status.HTTP_400_BAD_REQUEST)