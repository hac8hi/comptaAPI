from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from company_organization import views

urlpatterns = [
    path('company/', views.Company_List.as_view(), name='company-list'),
    path('company/<int:pk>/', views.Company_Detail.as_view(), name='company-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)