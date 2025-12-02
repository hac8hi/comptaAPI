from rest_framework import serializers
from .models import Payement_Methods, Payements, Payment_Allocations
from company_organization.models import Company
from contacts.models import Contacts

class Company_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Company

class Contact_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Contacts


class Payement_Method_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Payement_Methods
        fields = '__all__'

class Payement_Serializer(serializers.ModelSerializer):

    method = Payement_Method_Serializer(many=True)

    class Meta:
        model = Payements
        fields = '__all__'

class Payements_Allocation_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Payment_Allocations
        fields = '__all__'