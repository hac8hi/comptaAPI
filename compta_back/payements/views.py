from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import Payement_Serializer
from .models import Payements
# Create your views here.

class Payement_List(APIView):

    def get(self, request, company_id):
        payement = Payements.objects.filter(company_id=company_id)
        serializer = Payement_Serializer(payement)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, company_id):
        data = request.data
        data['company_id']= company_id
        serializer = Payement_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)