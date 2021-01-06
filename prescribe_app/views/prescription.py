from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny
from prescribe_app.serializers.patient_serializers import ( 

    PatientInformationSerializer, 

)
from prescribe_app.serializers.prescription_serializers import ( 

    PrescriptionSerializerView, 
    PrescriptionSerializerPostView,
    PrescriptionSerializerPost

)
from prescribe_app.models.patient_info import PatientInformation
from prescribe_app.models.prescription import Prescription


@api_view(['GET', 'POST'])
@renderer_classes([JSONRenderer])   
def prescription_view(request, format=None):

    if request.method == 'GET':
        prescription = Prescription.objects.all()
        serializer = PrescriptionSerializerView(prescription, many=True)
        
        print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'POST' :
        
        serializer = PrescriptionSerializerPostView(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("Data is saving")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Error in POST Method")
            content = {'Error': 'Invalid data'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def prescription_update_or_delete(request, pk):
    if request.method == 'GET':
        obj = Prescription.objects.filter(id=pk, active=True)
        serializer = PrescriptionSerializerView(instance=obj, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        obj = Prescription.objects.get(id=pk)
        serializer = PrescriptionSerializerPost(instance=obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            content = {'Error': 'Invalid data'}
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)

    elif request.method == 'DELETE' :
        obj = Prescription.objects.get(id=pk)
        obj.delete()
        return Response("Prescription successfully deleted")