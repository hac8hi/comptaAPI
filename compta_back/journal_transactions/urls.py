from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from journal_transactions import views

urlpatterns = [
    path('journal/', views.Journals_List.as_view(), name='journals_list'),
    path('journal/<str:pk>/', views.Journals_Detail.as_view(), name='journals_detail'),
    path('company/<str:company_id>/journal/<str:journal_id>/journal_entry/', views.Journal_Entries_List.as_view(), name='journal_entries_list'),
    path('company/<str:company_id>/journal/<str:journal_id>/journal_entry/<str:pk>', views.Journal_Entries_Detail.as_view(), name='journal_entries_detail'),
    path('journal_entry/<str:entry_id>/journal_entry_item/', views.Journal_Entry_Items_List.as_view(), name='journal_entry_items_list'),
    path('journal_entry/<str:entry_id>/journal_entry_item/<str:pk>', views.Journal_Entry_Items_Detail.as_view(), name='journal_entry_items_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)