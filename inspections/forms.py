# reports/forms.py

from django import forms
from .models import FuelStation, Tank, Nozzle
import jdatetime


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

class MyModelForm(forms.ModelForm):
    class Meta:
        model = FuelStation
        fields = ['title', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
    def clean_date(self):
            date = self.cleaned_data['date']
            # تبدیل تاریخ شمسی به میلادی
            gregorian_date = jdatetime.JalaliToGregorian(date.year, date.month, date.day).getGregorianList()
            return f"{gregorian_date[0]}-{gregorian_date[1]:02d}-{gregorian_date[2]:02d}"