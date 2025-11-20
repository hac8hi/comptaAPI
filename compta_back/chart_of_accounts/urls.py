from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from chart_of_accounts import views

urlpatterns = [
    path('company/<str:company_id>/account/', views.Account_List.as_view(), name='account-list'),
    path('company/<str:company_id>/account/<str:pk>/', views.Account_Detail.as_view(), name='account-detail'),
    path('account_types/', views.Account_Types_List.as_view(), name= 'account-type-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)