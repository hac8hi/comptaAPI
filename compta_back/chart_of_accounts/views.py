from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Accounts, Account_Types
from .serializers import Accounts_Serializer, Account_Types_Serializer

class Account_List(APIView):

    def get(self, request, company_id):

        accounts = Accounts.objects.get(company_id=company_id)
        serializer = Accounts_Serializer(accounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, company_id):

        data = request.data
        data['company_id'] = company_id
        serializer = Accounts_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Account_Detail(APIView):

    def get_object(self, company_id ,pk):
        
        try:
            return Accounts.objects.get(pk=pk, company_id=company_id)
        except Accounts.DoesNotExist:
            return Response({"Ce compte n'existe pas"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, company_id, pk):

        account = self.get_object(company_id, pk)
        serializer = Accounts_Serializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, company_id, pk):

        instance = self.get_object(company_id, pk)
        data = request.data
        data['company_id'] = company_id
        serializer = Accounts_Serializer(instance, data=request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, company_id, pk):

        account = self.get_object(company_id, pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Account_Types_List(APIView):

    def get(self, request):

        account_types = Account_Types.objects.all()
        serializer = Account_Types_Serializer(data=account_types, many=True)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)