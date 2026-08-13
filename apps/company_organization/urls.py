from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.company_organization import views

urlpatterns = [
    path('company/', views.CompanyList.as_view(), name='company-list'),
    path('company/<str:pk>/', views.CompanyDetail.as_view(), name='company-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)