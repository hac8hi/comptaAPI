from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

from company_organization.models import Company

# Create your models here.
class User(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='users_company')
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    ROLE = [
        ('admin', 'Admin'),
        ('accountant', 'Accountant'),
        ('viewer', 'Viewer')
    ]
    role = models.CharField(max_length=50, choices=ROLE, default='viewer')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class UserPermissions(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='permissions')
    MODULE = [
        ('invoicing', 'Invoicing'),
        ('payements', 'Payements'),
        ('reports', 'Reports'),
        ('chart_of_accounts', 'Chart of Accounts'),
        ('contacts', 'Contacts'),
        ('journal_entries', 'Journal Entries'),
        ('inventory', 'Inventory'),
        ('tax_management', 'Tax Management')
    ]
    module_name = models.CharField(max_length=50, choices=MODULE)
    can_create = models.BooleanField(default=False)
    can_read = models.BooleanField(default=True)
    can_update = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)