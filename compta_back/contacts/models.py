from django.db import models
from company_organization.models import Company

# Create your models here.
class Contact_Types(models.Model):

    type_name = models.CharField(max_length=50)

class Contacts(models.Model):

    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    contact_types_id = models.ForeignKey(Contact_Types, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True)
    tax_id = models.CharField(max_length=50, blank=True, null=True)
    payment_terms = models.IntegerField(blank=True, null=True)
    credit_limit = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Le contact {self.contact_name} de la société {self.company_id.name}"