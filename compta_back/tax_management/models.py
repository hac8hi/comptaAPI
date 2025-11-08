from django.db import models
from company_organization.models import Company
from chart_of_accounts.models import Accounts

# Create your models here.
class Tax_Rates(models.Model):

    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    tax_name = models.CharField(max_length=100)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2)
    tax_account_id = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"La société {self.company_id.name} - Taux de taxe: {self.tax_name} ({self.tax_rate}%)"