from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import Product_Serializer, Inventory_Transaction_Serializer
from .models import Products, Inventory_Transactions

# Create your views here.
class Product_List(APIView):

    def get(self, request, company_id):
        products = Products.objects.filter(company_id=company_id)
        serializer = Product_Serializer(products)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, company_id):
        data = request.data
        data['company_id'] = company_id
        serializer = Product_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class Product_Detail(APIView):

    def get_object(self, company_id, pk):
        try:
            return Products.objects.get(company_id=company_id, pk=pk)
        except Products.DoesNotExist:
            return Response({"Ce produit n'existe pas"}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, company_id, pk):
        product = self.get_object(company_id=company_id, pk=pk)
        serializer = Product_Serializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, company_id, pk):
        data = request.data
        data['company_id'] = company_id
        instance = self.get_object(company_id=company_id, pk=pk)
        serializer = Product_Serializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, company_id, pk):
        instance = self.get_object(company_id=company_id, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Inventory_Transaction_List(APIView):
    
    def get(self, request, product_id):
        transactions = Inventory_Transactions.objects.filter(product_id=product_id)
        serializer = Inventory_Transaction_Serializer(transactions)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, product_id):
        data = request.data
        data['product_id'] = product_id
        serializer = Inventory_Transaction_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class Inventory_Transaction_Detail(APIView):

    def get_object(self, product_id, pk):
        try:
            return Inventory_Transactions.objects.get(product_id=product_id, pk=pk)
        except Products.DoesNotExist:
            return Response({"Ce produit n'existe pas"}, status=status.HTTP_404_NOT_FOUND)
    def get(self, request, product_id, pk):
        transaction = self.get_object(product_id=product_id, pk=pk)
        serializer = Inventory_Transaction_Serializer(transaction)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, product_id, pk):
        data = request.data
        data['product_id'] = product_id
        instance = self.get_object(product_id=product_id, pk=pk)
        serializer = Inventory_Transaction_Serializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, product_id, pk):
        instance = self.get_object(product_id=product_id, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)