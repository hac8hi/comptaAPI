from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from company_organization.models import Company
from company_organization.serializers import Company_Serializer

class Company_List(APIView):

    def get(self, request):

        companies = Company.objects.all()
        serializer = Company_Serializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = Company_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Company_Detail(APIView):

    def get_object(self, pk):
        
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({"Cette société n'existe pas"}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk):

        company = self.get_object(pk)
        serializer = Company_Serializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):

        instance = Company.objects.get(pk=pk)
        serializer = Company_Serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):

        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)