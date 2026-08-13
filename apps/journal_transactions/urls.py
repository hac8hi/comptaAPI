from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from apps.journal_transactions import views

urlpatterns = [
    path('journal/', views.JournalList.as_view(), name='journal-list'),
    path('journal/<str:pk>/', views.JournalDetail.as_view(), name='journal-detail'),
    path('company/<str:company_id>/journal/<str:journal_id>/journal_entry/', views.JournalEntryList.as_view(), name='journal-entry-list'),
    path('company/<str:company_id>/journal/<str:journal_id>/journal_entry/<str:pk>', views.JournalEntryDetail.as_view(), name='journal-entry-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)