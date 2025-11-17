from .models import Journals, Journal_Entries, Journal_Entry_Items
from rest_framework import serializers

class Journals_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Journals
        fields = '__all__'

class Journal_Entries_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Journal_Entries
        fields = '__all__'

class Journal_Entry_Items_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Journal_Entry_Items
        fields = '__all__'