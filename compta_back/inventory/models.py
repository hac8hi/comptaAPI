from django.db import models
from company_organization.models import Company
from chart_of_accounts.models import Accounts
from invoicing.models import Invoices
from journal_transactions.models import Journal_Entries

# Create your models here.
class Products(models.Model):

    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    product_code = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    cost_price = models.DecimalField(max_digits=15, decimal_places=2)
    sale_price = models.DecimalField(max_digits=15, decimal_places=2)
    cogs_account_id = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Produit {self.product_name} ({self.product_code}) de la société {self.company_id.name} coutant {self.cost_price} et vendu à {self.sale_price}"

class Inventory_Transactions(models.Model):

    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    TRANSACTIONS = [
        ('achat', 'Achat'),
        ('vente', 'Vente'),
        ('ajustement', 'Ajustement'),
        ('retour', 'Retour'),
    ]
    transaction_type = models.CharField(max_length=15, choices=TRANSACTIONS)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_cost = models.DecimalField(max_digits=15, decimal_places=2)
    transaction_date = models.DateTime()
    invoice_id  = models.ForeignKey(Invoices, on_delete=models.CASCADE, null=True, blank=True)
    journal_entry_id = models.ForeignKey(Journal_Entries, on_delete=models.CASCADE, null=True, blank=True)
    REFERENCES = [
        ('invoice', 'Invoice'), 
        ('journal_entry', 'Journal Entry')
    ]
    reference_type = models.CharField(max_length=100, choices=REFERENCES, null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.transaction_type} pour le produit {self.product_id.product_name} de quantité {self.quantity} au coût unitaire de {self.unit_cost} le {self.transaction_date}"