from django.db import transaction
from rest_framework import serializers
from .models import Company, Company_Settings

class Company_Settings_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Company_Settings
        fields = ['setting_key', 'setting_value']

class Company_Serializer(serializers.ModelSerializer):

    settings = Company_Settings_Serializer(many=True, required=False)

    class Meta:
        model = Company
        exclude = ['created_at']
    
    def create(self, validated_data):

        settings_data = validated_data.pop('settings')

        with transaction.atomic():
            company = Company.objects.create(**validated_data)

            for setting_data in settings_data:
                Company_Settings.objects.create(company_id=company, **setting_data)
            
            return company
    
    def update(self, instance, validated_data):
        
        settings_data = validated_data.pop('settings')

        with transaction.atomic():
            instance = super().update(instance, validated_data)

            instance.settings.all().delete()

            if settings_data is not None:
                for setting_data in settings_data:
                    Company_Settings.objects.create(company_id=instance, **setting_data)
        
        return instance