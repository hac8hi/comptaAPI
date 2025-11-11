from rest_framework import serializers

from .models import Accounts, Account_Types
from company_organization.serializers import Company_Serializer

class Account_Types_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Account_Types
        fields = '__all__'

class Accounts_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Accounts
        fields = '__all__'