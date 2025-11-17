from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Journals, Journal_Entries, Journal_Entry_Items
from .serializers import Journals_Serializer, Journal_Entries_Serializer, Journal_Entry_Items_Serializer

# Create your views here.
class Journals_List(APIView):

    def get(self, request):

        journals = Journals.objects.all()
        serializer = Journals_Serializer(journals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        serializer = Journals_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Journals_Detail(APIView):

    def get_object(self, pk):

        try:
            return Journals.objects.get(pk=pk)
        except Journals.DoesNotExist:
            return Response({"Ce journal n'existe pas"}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):

        instance = self.get_object(pk=pk)
        serializer = Journals_Serializer(instance, data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):

        instance = self.get_object(pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Journal_Entries_List(APIView):

    def get(self, request, company_id, journal_id):
        
        journal_entries = Journal_Entries.objects.filter(company_id=company_id, journal_id=journal_id)
        serializer = Journal_Entries_Serializer(journal_entries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, journal_id):
        
        data = request.data
        data['journal_id'] = journal_id
        serializer = Journal_Entries_Serializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Journal_Entries_Detail(APIView):

    def get_object(self, company_id, journal_id, pk):

        try:
            return Journal_Entries.objects.get(pk=pk, company_id=company_id, journal_id=journal_id)
        except Journal_Entries.DoesNotExist:
            return Response({"Ce journal n'existe pas"}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, company_id, journal_id, pk):

        journal_entry = self.get_object(company_id=company_id, journal_id=journal_id, pk=pk)
        serializer = Journal_Entries_Serializer(journal_entry)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, company_id, journal_id, pk):

        instance = self.get_object(company_id=company_id, journal_id=journal_id, pk=pk)
        data = request.data
        data['company_id'] = company_id
        data['journal_id'] = journal_id
        serializer = Journal_Entries_Serializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, company_id, journal_id, pk):

        instance = self.get_object(company_id=company_id, journal_id=journal_id, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Journal_Entry_Items_List(APIView):

    def get(self, request, entry_id):

        journal_entry_items = Journal_Entry_Items.objects.filter(entry_id= entry_id)
        serializer = Journal_Entry_Items_Serializer(journal_entry_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, entry_id):

        data = request.data
        for item in data:
            item['entry_id'] = entry_id
        serializer = Journal_Entry_Items_Serializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Journal_Entry_Items_Detail(APIView):

    def get_object(self, entry_id, pk):

        try:
            return Journal_Entry_Items.objects.get(entry_id=entry_id, pk=pk)
        except Journal_Entry_Items.DoesNotExist:
            return Response({"Ce transaction n'existe pas"}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, entry_id, pk):

        journal_entry_items = self.get_object(entry_id=entry_id, pk=pk)
        serializer =Journal_Entry_Items_Serializer(journal_entry_items)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, entry_id, pk):

        instance = self.get_object(entry_id=entry_id, pk=pk)
        data = request.data
        data['entry_id'] = entry_id
        serializer = Journal_Entry_Items_Serializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, entry_id, pk):

        instance = self.get_object(entry_id=entry_id, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)