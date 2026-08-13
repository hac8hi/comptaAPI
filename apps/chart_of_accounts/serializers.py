
from rest_framework import serializers
from .models import Account, AccountType

class AccountTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountType
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):

    type = AccountTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        exclude = ['created_at']