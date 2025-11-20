from django.db import models
from company_organization.models import Company
import uuid

# Create your models here.
class Account_Types(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TYPES = [
        ('Actif', 'Actif'),
        ('Passif', 'Passif'),
        ('Actif/Passif', 'Actif/Passif'),
		('Charge', 'Charge'),
		('Produit', 'Produit'),
		('TVA', 'TVA'),
		('Autre', 'Autre'),
    ]
    type_name = models.CharField(max_length=50, choices=TYPES)
    BALANCE = [
        ('Debit', 'Debit'), 
        ('Credit', 'Credit'),
        ('Debit/Credit', 'Debit/Credit'),
        ]
    normal_balance = models.CharField(max_length=50, choices=BALANCE)

    def __str__(self):
        return self.type_name

class Accounts(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    account_name = models.CharField(max_length=255)
    account_type_id = models.ForeignKey(Account_Types, on_delete=models.CASCADE, related_name='type')
    parent_account_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_number} - {self.account_name} ({self.company_id.name})"