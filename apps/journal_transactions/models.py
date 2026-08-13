from django.db import models
from utils.models import AbstractModel
from apps.company_organization.models import Company
from apps.chart_of_accounts.models import Account
from auth.users_security.models import User

# Create your models here.
class Journal(AbstractModel):

    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.journal_name

class JournalEntry(AbstractModel):

    company = models.ForeignKey(Company, on_delete=models.CASCADE, )
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    entry_number = models.CharField(max_length=50)
    entry_date = models.DateField()
    reference = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    total_debit = models.DecimalField(max_digits=15, decimal_places=2)
    total_credit = models.DecimalField(max_digits=15, decimal_places=2)
    STATUS_CHOICES = [
    ('brouillon', 'Brouillon'),
    ('publié', 'Publié'),
    ('annulé', 'Annulé'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, default='draft')
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    posted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"L'écriture {self.entry_number} du {self.entry_date} dans le journal {self.journal_id.journal_name} avec total débit {self.total_debit} et total crédit {self.total_credit} de la société {self.company_id.name}"

class TransactionLine(AbstractModel):

    entry = models.ForeignKey(JournalEntry, on_delete=models.CASCADE, related_name='transaction_lines')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='account_transaction_lines')
    debit_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    credit_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    description = models.TextField(blank=True)
    line_number = models.IntegerField()

    def __str__(self):
        return f"Ligne {self.line_number} de l'écriture {self.entry_id.entry_number}: Compte {self.account_id.account_name}, Débit {self.debit_amount}, Crédit {self.credit_amount}"