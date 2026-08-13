from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.chart_of_accounts import views

urlpatterns = [
    path('company/<str:company_id>/account/', views.AccountList.as_view(), name='account-list'),
    path('company/<str:company_id>/account/<str:pk>/', views.AccountDetail.as_view(), name='account-detail'),
    path('account_types/', views.AccountTypeList.as_view(), name= 'account-type-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)