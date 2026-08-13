from django.db import models
from utils.models import AbstractModel
from apps.company_organization.models import Company
from auth.users_security.models import User
# Create your models here.

class Departement(AbstractModel):

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="departements")

    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Employee(AbstractModel):

    class GenderType(models.IntegerChoices):
        MALE = 0, "Homme"
        FEMALE = 1, "Femme"

    class RoleType(models.IntegerChoices):
        EMPLOYEE = 0, "Employee"
        ADMIN = 1, "Administrateur"
        MANAGER = 2, "Manager"

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, related_name="employees")

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.IntegerField(choices=GenderType.choices)

    function = models.CharField(max_length=32)
    role = models.IntegerField(choices=RoleType.choices, default=RoleType.EMPLOYEE)

    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=13, unique=True)
    cin = models.CharField(max_length=12, unique=True)
    dob = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.function} - {self.departement.name}"

    @property
    def get_full_name(self):
        return f"{str(self.first_name).upper()} {str(self.last_name).title() or ''}".strip()