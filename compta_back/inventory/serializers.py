from rest_framework import serializers
from .models import Products, Inventory_Transactions
from company_organization.models import Company

class Company_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_name']

class Product_Serializer(serializers.ModelSerializer):
    company_owner = Company_Serializer(read_only=True)

    class Meta:
        model = Products
        fields = '__all__'

class Inventory_Transaction_Serializer(serializers.ModelSerializer):
    product = Product_Serializer(read_only=True)

    class Meta:
        model = Inventory_Transactions
        fields = '__all__'