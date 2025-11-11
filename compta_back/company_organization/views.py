from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from company_organization.models import Company, Company_Settings
from company_organization.serializers import Company_Serializer, Company_Settings_Serializer

class Company_List(APIView):

    def get(self, request, format=None):

        companies = Company.objects.all()
        serializer = Company_Serializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

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
    
    def get(self, pk):

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
    
    def delete(self, pk):

        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Company_Settings_List(APIView):

    def get(self, fk):

        settings = Company_Settings.objects.get(company_id=fk)
        serializer = Company_Settings_Serializer(settings, many=True)
        return Response(serializer.data)

    def post(self, request, fk):

        data = request.data
        data['company_id'] = fk
        serializer = Company_Settings_Serializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Company_Settings_Detail(APIView):

    def get_object(self, fk, pk):
        
        try:
            return Company_Settings.objects.get(pk=pk, company_id=fk)
        except Company_Settings.DoesNotExist:
            return Response({"Ce paramètre de société n'existe pas"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, fk, pk):

        instance = self.get_object(fk, pk)
        data = request.data
        data['company_id'] = fk
        serializer = Company_Settings_Serializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, fk, pk):

        setting = self.get_object(fk, pk)
        setting.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)