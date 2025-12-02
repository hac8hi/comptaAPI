from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from inventory import views

urlpatterns = [
    path('company/<str:company_id>/product/', views.Product_List.as_view(), name='product_list'),
    path('company/<str:company_id>/product/<str:pk>/', views.Product_Detail.as_view(), name='product_detail'),
    path('product/<str:product_id>/transaction/', views.Inventory_Transaction_List.as_view(), name='transaction_list'),
    path('product/<str:product_id>/transaction/<str:pk>/', views.Inventory_Transaction_Detail.as_view(), name='transaction_detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)