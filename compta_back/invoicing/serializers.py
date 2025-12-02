from django.db import transaction
from rest_framework import serializers
from .models import Invoices, Invoices_Lines
from company_organization.models import Company
from contacts.models import Contacts

class Contact_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['contact_name', 'email', 'phone', 'address']

class Company_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_name', 'email', 'phone', 'address']

class Invoices_Lines_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Invoices_Lines
        exclude = ['id']

class Invoices_Serializer(serializers.ModelSerializer):

    company_contact = Company_Serializer(read_only=True)
    contact = Contact_Serializer(read_only=True)
    invoice_lines = Invoices_Lines_Serializer(many=True, required=False)

    class Meta:
        model = Invoices
        field = '__all__'
    
    def create(self, validated_data):
        invoice_lines = validated_data.pop('invoice_lines')

        with transaction.atomic():
            invoice = Invoices.objects.create(**validated_data)

            for invoice_line in invoice_lines:
                Invoices_Lines.objects.create(invoice_id=invoice, **invoice_line)
        
        return invoice
    
    def update(self, instance, validated_data):
        invoice_lines = validated_data.pop('invoice_lines')

        with transaction.atomic():
            instance = super().update(instance, validated_data)

            instance.invoice_lines.all().delete()

            if invoice_lines is not None:
                for invoice_line in invoice_lines:
                    Invoices_Lines.objects.create(invoice_id=instance, **invoice_line)

        return instance