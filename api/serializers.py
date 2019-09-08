from rest_framework import serializers
from .models import PillDetails


class dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PillDetails
        fields = ("medication_name", "pills_per_dose",
                  "doses_per_day", "total_qty", "num_mg")
