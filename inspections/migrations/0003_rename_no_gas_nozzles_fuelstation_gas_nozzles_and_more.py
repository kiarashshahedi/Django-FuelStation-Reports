# Generated by Django 5.0.6 on 2024-06-28 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0002_fuelstation_no_gas_nozzles_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fuelstation',
            old_name='no_gas_nozzles',
            new_name='gas_nozzles',
        ),
        migrations.RenameField(
            model_name='fuelstation',
            old_name='no_gasoline_nozzles',
            new_name='gasoline_nozzles',
        ),
    ]
