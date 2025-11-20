from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from contacts import views

urlpatterns = [
    path('company/<str:company_id>/contacts', views.Contacts_List.as_view(), name='contacts-list'),
    path('company/<str:company_id>/contacts/<str:pk>', views.Contact_Detail.as_view(), name='contact-detail'),
    path('contact_types/', views.Contact_Types_List.as_view(), name='contact-type-list')
]

urlpatterns = format_suffix_patterns(urlpatterns)