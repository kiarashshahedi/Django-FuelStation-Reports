# reports/forms.py

from django import forms
from .models import FuelStation, Tank, Nozzle

class FuelStationForm(forms.ModelForm):
    class Meta:
        model = FuelStation
        fields = '__all__'

class TankForm(forms.ModelForm):
    class Meta:
        model = Tank
        fields = '__all__'

class NozzleForm(forms.ModelForm):
    class Meta:
        model = Nozzle
        fields = '__all__'
