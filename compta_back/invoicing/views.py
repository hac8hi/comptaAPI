from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Invoices
from .serializers import Invoices_Serializer

class Invoice_List(APIView):

    def get(self, request, company_id):
        invoice = Invoices.objects.filter(company_id=company_id)
        serializer = Invoices_Serializer(invoice)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, company_id):
        data = request.data
        data['company_id'] = company_id
        serializer = Invoices_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Invoice_Detail(APIView):

    def get_object(self, company_id, pk):
        try:
            return Invoices.objects.get(company_id=company_id, pk=pk)
        except Invoices.DoesNotExist:
            return Response({"Cette facture n'existe pas"}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, company_id, pk):
        invoice = self.get_object(company_id=company_id, pk=pk)
        serializer = Invoices_Serializer(invoice)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, company_id, pk):
        data = request.data
        data['company_id'] = company_id
        instance = self.get_object(company_id=company_id, pk=pk)
        serializer = Invoices_Serializer(instance, data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)