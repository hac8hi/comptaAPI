from rest_framework import serializers
from django.db import transaction
from .models import Company_Settings
from .serializers import Company_Serializer, Company_Settings_Serializer

@transaction.atomic()
def post_company(company_data):

    company_settings_data = company_data.pop('settings', '')
    
    company = Company_Serializer(data=company_data)
    if not company.is_valid():
        raise serializers.ValidationError(company.errors)
    company_instance = company.save()

    for company_setting_data in company_settings_data:
        company_setting_data['company_id'] = company_instance.id
    company_settings = Company_Settings_Serializer(data=company_settings_data, many=True)
    if not company_settings.is_valid():
        raise serializers.ValidationError(company_settings.errors)
    company_settings.save()

    return company.data

@transaction.atomic()
def update_company(instance, company_data):
    
    company_settings_data = company_data.pop('settings', '')

    company = Company_Serializer(instance, data=company_data)

    if not company.is_valid():
        raise serializers.ValidationError(company.errors)
    company.save()

    company_settings = []

    for company_setting_data in company_settings_data:
        setting_instance = Company_Settings.objects.get(pk=company_setting_data['id'])
        company_setting = Company_Settings_Serializer(setting_instance, data=company_setting_data)
        if not company_setting.is_valid():
            raise serializers.ValidationError(company_setting.errors)
        company_setting.save()
        company_settings.append(company_setting.data)
    
    return company.data,