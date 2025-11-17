from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from contacts import views

urlpatterns = [
    path('company/<str:fk>/contacts', views.Contacts_List.as_view(), name='contacts-list'),
    path('company/<str:fk>/contacts/<str:pk>', views.Contact_Detail.as_view(), name='contact-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)