from django import forms
from vehicle.models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ["number_plate", "nick_name", "vehcile_type", "vehcile_model"]
