from rest_framework import serializers

from prescribe_app.models.notes import Notes



class NotesSerializersPost(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['notes']


class NotesSerializersView(serializers.ModelSerializer):
    date_created = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    class Meta:
        model = Notes
        fields = ['id', 'notes', 'date_created']