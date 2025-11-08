from django.db import models
from company_organization.models import Company

# Create your models here.
class Financial_report(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    REPORTS = [
        ('bilan', 'Bilan'),
        ('compte_de_resultat', 'Compte de résultat'),
        ('flux_de_tresorerie', 'Flux de trésorerie'),
        ('balance_comptable', 'Balance comptable'),
    ]
    report_type = models.CharField(max_length=100, choices=REPORTS)
    report_date = models.DateField()
    report_data = models.JSONField()
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rapport financier de type {self.report_type} pour la société {self.company.name} généré le {self.generated_at}"