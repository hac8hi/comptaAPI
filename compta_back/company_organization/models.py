from django.db import models
import uuid

# Create your models here.
class Company(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_name = models.CharField(max_length=255)
    tax_id = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    fiscal_year_start = models.DateField(blank=True, null=True)
    currency_code = models.CharField(max_length=3, default='USD')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name

class Company_Settings(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='settings')
    setting_key = models.CharField(max_length=100, blank=True)
    setting_value = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Paramètre {self.setting_key} pour la société {self.company_id.company_name}"