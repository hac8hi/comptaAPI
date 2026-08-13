from django.db import transaction
from rest_framework import serializers
from apps.company_organization.models import CustomerCategory, Company

class CustomerCategory(serializers.ModelSerializer):

    class Meta:
        model = CustomerCategory
        exclude = ["created_at", "updated_at"]

class CompanySerializer(serializers.ModelSerializer):
    customer_category = CustomerCategory()

    class Meta:
        model = Company
        exclude = ["created_at", "updated_at"]