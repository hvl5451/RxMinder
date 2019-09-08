from django.db import models

# Create your models here.


class PillDetails(models.Model):
    medication_name = models.CharField(max_length=250, null=True)
    pills_per_dose = models.CharField(max_length=250, null=True)
    doses_per_day = models.CharField(max_length=250, null=True)
    total_qty = models.CharField(max_length=10, null=True)
    num_mg = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.medication_name
