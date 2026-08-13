from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Journal, JournalEntry
from .serializers import JournalSerializer, JournalEntrySerializer

# Create your views here.
class JournalList(APIView):

    def get(self, request):

        journals = Journal.objects.all()
        serializer = JournalSerializer(journals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = JournalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JournalDetail(APIView):

    def get_object(self, pk):

        try:
            return Journal.objects.get(pk=pk)
        except Journal.DoesNotExist:
            return Response({"Ce journal n'existe pas"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):

        instance = self.get_object(pk=pk)
        serializer = JournalSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):

        instance = self.get_object(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class JournalEntryList(APIView):

    def get(self, request, company_id, journal_id):
        
        journal_entries = JournalEntry.objects.filter(company_id=company_id, journal_id=journal_id)
        serializer = JournalEntrySerializer(journal_entries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, journal_id):
        
        data = request.data
        data['journal_id'] = journal_id
        serializer = JournalEntrySerializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JournalEntryDetail(APIView):

    def get_object(self, company_id, journal_id, pk):

        try:
            return JournalEntry.objects.get(pk=pk, company_id=company_id, journal_id=journal_id)
        except JournalEntry.DoesNotExist:
            return Response({"Ce journal n'existe pas"}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, company_id, journal_id, pk):

        journal_entry = self.get_object(company_id=company_id, journal_id=journal_id, pk=pk)
        serializer = JournalEntrySerializer(journal_entry)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, company_id, journal_id, pk):

        instance = self.get_object(company_id=company_id, journal_id=journal_id, pk=pk)
        data = request.data
        data['company_id'] = company_id
        data['journal_id'] = journal_id
        serializer = JournalEntrySerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, company_id, journal_id, pk):

        instance = self.get_object(company_id=company_id, journal_id=journal_id, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)