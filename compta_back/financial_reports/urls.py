from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from financial_reports import views

urlpatterns = [
    path('company/<str:company_id>/financial_report/', views.Financial_Report_List.as_view(), name='financial_report_list'),
    path('company/<str:company_id>/financial_report/<str:pk>', views.Financial_Report_Detail.as_view(), name='financial_report_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)