from django.db import transaction
from .models import Journal, JournalEntry, TransactionLine
from apps.chart_of_accounts.models import Account
from rest_framework import serializers

class JournalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Journal
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['account_number', 'account_name']

class TransactionLineSerializer(serializers.ModelSerializer):

    account = AccountSerializer(read_only=True)

    class Meta:
        model = TransactionLine
        exclude = ['id', 'entry_id']

class JournalEntrySerializer(serializers.ModelSerializer):
    
    items = TransactionLineSerializer(many=True, required=False)

    class Meta:
        model = JournalEntry
        fields = '__all__'
    
    def create(self, validated_data):
        
        items = validated_data.pop('items')

        with transaction.atomic():
            entry = JournalEntry.objects.create(**validated_data)

            for item in items:
                TransactionLine.objects.create(entry_id=entry, **item)
        
        return entry
    
    def update(self, instance, validated_data):

        items = validated_data.pop('items')

        with transaction.atomic():
            instance = super().update(instance, validated_data)

            instance.items.all().delete()

            if items is not None:
                for item in items:
                    TransactionLine.objects.create(entry_id=instance, **item)
            
            return instance