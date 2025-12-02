from rest_framework import serializers
from .models import Financial_Report
from company_organization.models import Company

class Company_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['company_name']

class Financial_Report_Serializer(serializers.ModelSerializer):

    name_of_company = Company_Serializer(read_only=True)

    class Meta:
        model = Financial_Report
        fields = '__all__'