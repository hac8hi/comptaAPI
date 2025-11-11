from rest_framework import serializers
from .models import Contacts, Contact_Types

class Contact_Types_Serializer(serializers.ModelSerializer):

    class Metha:
        model = Contact_Types
        fields = '__all__'

class Contacts_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = '__all__'