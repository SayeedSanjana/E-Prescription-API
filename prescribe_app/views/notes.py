from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny

from prescribe_app.models.patient_info import PatientInformation
from prescribe_app.models.notes import Notes

from prescribe_app.serializers.notes_serializers import ( 
    NotesSerializersView,
    NotesSerializersPost

)

@api_view(['GET', 'POST'])
def notes_list_and_create_view(request):
    if request.method == 'GET' :
        notes = Notes.objects.all()
        serializer  = NotesSerializersView(notes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NotesSerializersPost(data=request.data)
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
def notes_info_detail_and_update(request, pk):
    
    if request.method == 'GET':
        patient = PatientInformation.objects.get(id=pk)
        notes = Notes.objects.get(patient=patient)
        
        serializer = NotesSerializersView(instance=notes)
        return Response(serializer.data)
    

    elif request.method == 'PUT':
        obj = Notes.objects.get(id=pk)
        serializer = NotesSerializersPost(instance=obj, data=request.data)
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