from rest_framework import serializers
from chart_of_accounts.models import Account, AccountType

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'
    
class AccountTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountType
        fields = '__all__'