from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from users_security.views import LoginView, RegisterView, RefreshView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/refresh/', RefreshView.as_view(), name='token_refresh'),
]

urlpatterns = format_suffix_patterns(urlpatterns)