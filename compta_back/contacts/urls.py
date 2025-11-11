from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from contacts import views

urlpatterns = [
    path('company/<int:fk>/contacts', views.Contacts_List.as_view(), name='contacts-list'),
    path('company/<int:fk>/contacts/<int:pk>', views.Contact_Detail.as_view(), name='contact-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)