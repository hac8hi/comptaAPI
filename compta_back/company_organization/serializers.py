from rest_framework import serializers
from .models import Company, Company_Settings

class Company_Settings_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Company_Settings
        fields = '__all__'

class Company_Serializer(serializers.ModelSerializer):

    settings = Company_Settings_Serializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = '__all__'