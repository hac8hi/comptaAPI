from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Financial_Report
from .serializers import Financial_Report_Serializer

# Create your views here.
class Financial_Report_List(APIView):

    def get(self, request, company_id):

        report = Financial_Report.objects.filter(company_id=company_id)
        serializer = Financial_Report_Serializer(report)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, company_id):

        data = request.data
        data['company_id'] = company_id
        serializer = Financial_Report_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Financial_Report_Detail(APIView):

    def get_object(self, company_id, pk):

        try:
            return Financial_Report.objects.get(company_id=company_id, pk=pk)
        except Financial_Report.DoesNotExist:
            return Response({"Ce rapport n'existe pas"} ,status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, company_id, pk):

        report = self.get_object(company_id=company_id, pk=pk)
        serializer = Financial_Report_Serializer(report)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, company_id, pk):

        instance = self.get_object(company_id=company_id, pk=pk)
        data = request.data
        data['company_id'] = company_id
        serializer = Financial_Report_Serializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, company_id, pk):

        instance = self.get_object(company_id=company_id, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)