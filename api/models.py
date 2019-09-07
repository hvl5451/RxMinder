from django.db import models

# Create your models here.


class PillDetails(models.Model):
    client_id = models.CharField(max_length=250, null=True)
    medicine_name = models.CharField(max_length=250, null=True)
    pill_per_dose = models.CharField(max_length=250, null=True)
    doses_per_day = models.CharField(max_length=250, null=True)
    total_qty = models.CharField(max_length=10, null=True)

    def __str__(self):
        return "{} - {}".format(self.client_id, self.medicine_name)
