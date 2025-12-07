from rest_framework import serializers
from .models import Payement_Methods, Payements, Payment_Allocations
from company_organization.models import Company
from contacts.models import Contacts

class Company_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ['company_name']

class Contact_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts
        fields = ['email', 'phone', 'address']


class Payement_Method_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Payement_Methods
        fields = '__all__'

class Payements_Allocation_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Payment_Allocations
        fields = '__all__'

class Payement_Serializer(serializers.ModelSerializer):

    company_for_payement = Company_Serializer(read_only=True)
    method = Payement_Method_Serializer(many=True)
    contact_for_payement = Contact_Serializer(read_only=True)
    allocation = Payements_Allocation_Serializer()

    class Meta:
        model = Payements
        fields = '__all__'