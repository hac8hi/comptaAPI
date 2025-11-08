from django.db import models
from company_organization import Company

# Create your models here.
class Users(models.Model):

    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    ROLES = [
        ('administrateur', 'Administrateur'),
        ('comptable', 'Comptable'),
        ('Observateur', 'Observateur'),
    ]
    role = models.CharField(max_length=50, choices=ROLES, default='Observateur')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"L'utilisateur {self.username} ({self.full_name}) appartient à la société {self.company_id.name}"

class User_Permissions(models.Model):

    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    module = models.CharField(max_length=100)
    can_create = models.BooleanField(default=False)
    can_read = models.BooleanField(default=True)
    can_update = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)

    def __str__(self):
        return f"L'utilisateur {self.user_id.username} - Module: {self.module} peut créer: {self.can_create}, lire: {self.can_read}, mettre à jour: {self.can_update}, supprimer: {self.can_delete}"