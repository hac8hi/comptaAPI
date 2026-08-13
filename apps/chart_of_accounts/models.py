from django.db import models
from utils.models import AbstractModel
from apps.company_organization.models import Company

# Create your models here.
class AccountType(AbstractModel):

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

class Account(AbstractModel):

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_accounts")
    number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    type = models.ForeignKey(AccountType, on_delete=models.CASCADE, related_name='accounts')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.account_number} - {self.account_name} ({self.company_id.name})"