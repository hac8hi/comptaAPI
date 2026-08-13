from django.apps import AppConfig


class UsersSecurityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth.users_security'
    label = 'users_security'