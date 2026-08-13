
from django.db import models
from utils.models import AbstractModel
from auth.users_security.models import User

# Create your models here.
class CustomerCategory(AbstractModel):

    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.code} : {self.name}'


class Company(AbstractModel):

    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    headers = models.JSONField()
    stat_number = models.CharField(max_length=50)
    tax_identification = models.CharField(max_length=50)
    trade_register = models.CharField(max_length=50)
    economic_card = models.CharField(max_length=50, blank=True, null=True)
    bank = models.CharField(max_length=50, blank=True, null=True)
    customer_category = models.ForeignKey(CustomerCategory, on_delete=models.CASCADE, related_name="companies", blank=True, null=True)
    is_customer = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name