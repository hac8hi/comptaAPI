from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from journal_transactions import views

urlpatterns = [
    path('company/<str:company_id>/invoice/', views.Journal_Entries_List.as_view(), name='invoice_list'),
    path('company/<str:company_id>/invoice/<str:pk>', views.Journal_Entries_Detail.as_view(), name='invoice_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)