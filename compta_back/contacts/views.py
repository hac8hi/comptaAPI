from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Contacts, Contact_Types
from .serializers import Contacts_Serializer, Contact_Types_Serializer

class Contacts_List(APIView):

    def get(self, request, company_id):

        contacts = Contacts.objects.get(company_id=company_id)
        serializer = Contacts_Serializer(data=contacts, many=True)
        if serializer.valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, company_id):

        data = request.data
        data['company_id'] = company_id
        serializer = Contacts_Serializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Contact_Detail(APIView):

    def get_object(self, company_id, pk):

        try:
            return Contacts.objects.get(pk=pk, company_id=company_id)
        except Contacts.DoesNotExist:
            return Response({"Ce contact n'existe pas"}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, company_id, pk):

        contact = self.get_object(company_id, pk)
        serializer = Contacts_Serializer(data=contact)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, company_id, pk):

        instance = self.get_object(company_id, pk)
        data = request.data
        data['company_id'] = company_id
        serializer = Contacts_Serializer(instance, data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, company_id, pk):

        contact = self.get_object(company_id, pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Contact_Types_List(APIView):

    def get(self, request):
        
        contact_types = Contact_Types.objects.all()
        serializer = Contact_Types_Serializer(data=contact_types, many=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)