from django.db import models
from company_organization.models import Company
from contacts.models import Contacts
from chart_of_accounts.models import Accounts
from invoicing.models import Invoices

# Create your models here.
class Payement_Methods(models.Model):

    METHODS = [
        ('espèce', 'espèce'),
        ('chèque', 'Chèque'),
        ('carte de crédit', 'Carte de crédit'),
        ('tranfert banquaire', 'Tranfert banquaire')
    ]
    method_name = models.CharField(max_length=50, choices=METHODS)

    def __str__(self):
        return self.method_name

class Payements(models.Model):

    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    contact_id = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    payement_date = models.DateField()
    payement_method_id = models.ForeignKey(Payement_Methods, on_delete=models.CASCADE)
    reference_number = models.CharField(max_length=100, blank=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    account_id = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Le payement de {self.amount} le {self.payement_date} pour {self.contact_id.name} de la société {self.company_id.name}"

class Payment_Allocations(models.Model):

    payement_id = models.ForeignKey(Payements, on_delete=models.CASCADE)
    invoice_id = models.ForeignKey(Invoices, on_delete=models.CASCADE)
    allocated_amount = models.DecimalField(max_digits=15, decimal_places=2)
    allocation_date = models.DateField()

    def __str__(self):
        return f"Allocation de {self.allocated_amount} du payement {self.payement_id.id} à la facture {self.invoice_id.id}"