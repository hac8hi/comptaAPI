from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from chart_of_accounts import views

urlpatterns = [
    path('company/<int:fk>/account/', views.Account_List.as_view(), name='account-list'),
    path('company/<int:fk>/account/<int:pk>/', views.Account_Detail.as_view(), name='account-detail'),
    path('account_type/', views.Account_Types_List.as_view(), name= 'account-type-list'),
    path('company/<int:fk>/account/<int:pk>/type/', views.Account_Types_Detail.as_view(), name='account-type-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)