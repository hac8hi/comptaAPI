from django.db import models
from company_organization.models import Company
from chart_of_accounts.models import Accounts
from contacts.models import Contacts

# Create your models here.
class Journals(models.Model):
    journal_name = models.CharField(max_length=100)
    journal_code = models.CharField(max_length=10)

    def __str__(self):
        return self.journal_name

class Journal_Entries(models.Model):

    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    journal_id = models.ForeignKey(Journals, on_delete=models.CASCADE)
    entry_number = models.CharField(max_length=50)
    entry_date = models.DateField()
    reference = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    total_debit = models.DecimalField(max_digits=15, decimal_places=2)
    total_credit = models.DecimalField(max_digits=15, decimal_places=2)
    STATUS_CHOICES = [
    ('brouillon', 'Brouillon'),
    ('publié', 'Publié'),
    ('annulé', 'Annulé'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_by = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    posted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"L'écriture {self.entry_number} du {self.entry_date} dans le journal {self.journal_id.journal_name} avec total débit {self.total_debit} et total crédit {self.total_credit} de la société {self.company_id.name}"

class Journal_Entry_Items(models.Model):

    entry_id = models.ForeignKey(Journal_Entries, on_delete=models.CASCADE)
    account_id = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    contact_id = models.ForeignKey(Contacts, on_delete=models.CASCADE, blank=True, null=True)
    debit_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    credit_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    description = models.TextField(blank=True)
    line_number = models.IntegerField(blank=True)

    def __str__(self):
        return f"Ligne {self.line_number} de l'écriture {self.entry_id.entry_number}: Compte {self.account_id.account_name}, Débit {self.debit_amount}, Crédit {self.credit_amount}"