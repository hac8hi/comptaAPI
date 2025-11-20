from django.db import transaction
from .models import Journals, Journal_Entries, Journal_Entry_Items
from chart_of_accounts.models import Accounts
from rest_framework import serializers

class Journals_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Journals
        fields = '__all__'

class Account_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Accounts
        fields = ['account_number', 'account_name']

class Journal_Entry_Items_Serializer(serializers.ModelSerializer):

    account = Account_Serializer(read_only=True)

    class Meta:
        model = Journal_Entry_Items
        exclude = ['id', 'entry_id']

class Journal_Entries_Serializer(serializers.ModelSerializer):
    
    items = Journal_Entry_Items_Serializer(many=True, required=False)

    class Meta:
        model = Journal_Entries
        fields = '__all__'
    
    def create(self, validated_data):
        
        items = validated_data.pop('items')

        with transaction.atomic():
            entry = Journal_Entries.objects.create(**validated_data)

            for item in items:
                Journal_Entry_Items.objects.create(entry_id=entry, **item)
        
        return entry
    
    def update(self, instance, validated_data):

        items = validated_data.pop('items')

        with transaction.atomic():
            instance = super().update(instance, validated_data)

            instance.items.all().delete()

            if items is not None:
                for item in items:
                    Journal_Entry_Items.objects.create(entry_id=instance, **item)
            
            return instance