from django.db import models
import django_jalali.db.models as jmodels
from django.db import transaction
from django.db.models import Sum




class FuelStation(models.Model):
    name = models.CharField(max_length=200)
    
    gasoline_tanks = models.IntegerField()
    gas_tanks = models.IntegerField()
    
    gasoline_nozzles = models.IntegerField()  
    gas_nozzles = models.IntegerField() 
    
    gasoline_beginning = models.FloatField()
    gas_beginning = models.FloatField()
    
    gasoline_received = models.FloatField()
    gas_received = models.FloatField()
    
    electronic_gasoline_sales = models.FloatField()
    electronic_gas_sales = models.FloatField()
    
    start_date = jmodels.jDateField()
    end_date = jmodels.jDateField()
    
    controller = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def gasoline_mechanical_sales(self):
        # Sum up mechanical sales of all gasoline nozzles for this station
        total_sales = 0.0
        gasoline_nozzles = Nozzle.objects.filter(station=self, type='gasoline')
        for nozzle in gasoline_nozzles:
            total_sales += nozzle.mechanical_sales()
        return total_sales
    
    def gas_mechanical_sales(self):
        # Sum up mechanical sales of all gasoline nozzles for this station
        total_sales = 0.0
        gas_nozzles = Nozzle.objects.filter(station=self, type='gas')
        for nozzle in gas_nozzles:
            total_sales += nozzle.mechanical_sales()
        return total_sales
    
    def gasoline_end_inventory(self):
        total_amount = 0.0
        gasoline_tanks = Tank.objects.filter(station=self, type='gasoline')
        for tank in gasoline_tanks:
            total_amount += tank.amount_tank()
        return total_amount

    def gas_end_inventory(self):
        total_amount = 0.0
        gas_tanks = Tank.objects.filter(station=self, type='gas')
        for tank in gas_tanks:
            total_amount += tank.amount_tank()
        return total_amount

    def total_tank_amount(self):
        total_amount = Tank.objects.filter(station=self, type='gasoline').aggregate(total=Sum('amount'))['total']
        print(f"Aggregated total amount: {total_amount}")  # Debug print
        return total_amount if total_amount is not None else 0.0
    
    def total_gs_tank_amount(self):
        total_amount = Tank.objects.filter(station=self, type='gas').aggregate(total=Sum('amount'))['total']
        print(f"Aggregated total amount: {total_amount}")  # Debug print
        return total_amount if total_amount is not None else 0.0


class Tank(models.Model):
    station = models.ForeignKey(FuelStation, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=[('gasoline', 'Gasoline'), ('gas', 'Gas')])
    amount = models.FloatField()
    
    def amount_tank(self):
        return self.amount
    
    def __str__(self):
        return f"{self.type} tank with {self.amount} amount"

class Nozzle(models.Model):
    station = models.ForeignKey(FuelStation, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=[('gasoline', 'Gasoline'), ('gas', 'Gas')])
    start_totalizer = models.FloatField()
    end_totalizer = models.FloatField()

    def mechanical_sales(self):
        return self.end_totalizer - self.start_totalizer

    def __str__(self):
        return f"{self.type} nozzle with start: {self.start_totalizer} and end: {self.end_totalizer}"