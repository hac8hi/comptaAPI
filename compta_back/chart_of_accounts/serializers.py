
from rest_framework import serializers
from .models import Accounts, Account_Types

class Account_Types_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Account_Types
        fields = '__all__'

class Accounts_Serializer(serializers.ModelSerializer):

    type = Account_Types_Serializer(many=True, read_only=True)

    class Meta:
        model = Accounts
        exclude = ['created_at']