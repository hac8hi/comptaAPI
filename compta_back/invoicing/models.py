from django.db import models
from company_organization.models import Company
from contacts.models import Contacts
from chart_of_accounts.models import Accounts

# Create your models here.
class Invoices(models.Model):
    
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    contact_id = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=50, unique=True)
    invoice_date = models.DateField()
    due_date = models.DateField()
    TYPES = [
        ('Ventes', 'ventes'),
        ('Achats', 'achats'),
    ]
    invoice_type = models.CharField(max_length=10, choices=TYPES)
    STATUS_CHOICES = [
    ('brouillon', 'Brouillon'),
    ('envoyé', 'Envoyé'),
    ('payé', 'Payé'),
    ('en retard', 'En retard'),
    ('annulé', 'Annulé'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Brouillon')
    subtotal = models.DecimalField(max_digits=15, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    balance_due = models.DecimalField(max_digits=15, decimal_places=2, editable=False)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.balance_due = self.total_amount - self.amount_paid
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"La facture numero : {self.invoice_number} du {self.invoice_date} de type {self.invoice_type} avec un montant payé de {self.amount_paid} sur un montant total de {self.total_amount}"

class Invoices_Lines(models.Model):

    invoice_id = models.ForeignKey(Invoices, on_delete=models.CASCADE)
    account_id = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    item_description = models.TextField()
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    line_total = models.DecimalField(max_digits=15, decimal_places=2, editable=False)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def save(self, *args, **kwargs):
        self.line_total = self.quantity * self.unit_price
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Ligne de la facture {self.invoice_id.invoice_number}: {self.item_description}, Quantité: {self.quantity}, Prix unitaire: {self.unit_price}, Total ligne: {self.line_total}"