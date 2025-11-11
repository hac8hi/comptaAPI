from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Contacts, Contact_Types
from .serializers import Contacts_Serializer, Contact_Types_Serializer

class Contacts_List(APIView):

    def get(self, fk):

        contacts = Contacts.objects.get(company_id=fk)
        serializer = Contacts_Serializer(data=contacts, many=True)
        if serializer.valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, fk, request):

        data = request.data
        data['company_id'] = fk
        serializer = Contacts_Serializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Contact_Detail(APIView):

    def get_object(self, fk, pk):

        try:
            return Contacts.objects.get(pk=pk, company_id=fk)
        except Contacts.DoesNotExist:
            return Response({"Ce paramètre de société n'existe pas"}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, fk, pk):

        contact = self.get_object(fk, pk)
        serializer = Contacts_Serializer(data=contact)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, fk, pk, request):

        instance = self.get_object(fk, pk)
        data = request.data
        data['company_id'] = fk
        serializer = Contacts_Serializer(instance, data=data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, fk, pk):

        contact = self.get_object(fk, pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Contact_Types_List(APIView):

    def get(self):
        contact_types = Contact_Types.objects.all()
        serializer = Contact_Types_Serializer(data=contact_types, many=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Contact_Types_Detail(APIView):

    def get_object(self, pk):
        
        return Contact_Types.objects.get(pk=pk)
    
    def get(self, fk, pk):

        contact = Contact_Detail.get_object(fk, pk)
        contact_type = self.get_object(contact.contact_types_id)
        serializer = Contact_Types_Serializer(data=contact_type)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)