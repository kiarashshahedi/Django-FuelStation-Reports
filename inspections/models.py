from django.db import models

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
    
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Tank(models.Model):
    station = models.ForeignKey(FuelStation, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=[('gasoline', 'Gasoline'), ('gas', 'Gas')])
    amount = models.FloatField()

class Nozzle(models.Model):
    station = models.ForeignKey(FuelStation, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=[('gasoline', 'Gasoline'), ('gas', 'Gas')])
    start_totalizer = models.FloatField()
    end_totalizer = models.FloatField()

    def mechanical_sales(self):
        return self.end_totalizer - self.start_totalizer
