from company_organization.models import Company
from company_organization.serializers import Company_Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import post_company, update_company

# Create your views here.
class Company_List(APIView):

    def get(self, request, format=None):

        companies = Company.objects.all()
        serializer = Company_Serializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        try:
            response = post_company(request.data)
            return Response(response, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({str(e)}, status=status.HTTP_400_BAD_REQUEST)

class Company_Detail(APIView):

    def get_object(self, pk):
        
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({"Cette société n'existe pas"}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk, format=None):

        company = self.get_object(pk)
        serializer = Company_Serializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):

        try:
            company = self.get_object(pk)
            response = update_company(company, request.data)
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):

        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)