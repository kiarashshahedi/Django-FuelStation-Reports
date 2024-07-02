from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import transaction
from .models import FuelStation
import jdatetime

def create_station(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        # تبدیل تاریخ شمسی به میلادی
        start_date_parts = list(map(int, start_date.split('-')))
        end_date_parts = list(map(int, end_date.split('-')))

        gregorian_start_date = jdatetime.date(
            start_date_parts[0],
            start_date_parts[1],
            start_date_parts[2]
        ).togregorian()

        gregorian_end_date = jdatetime.date(
            end_date_parts[0],
            end_date_parts[1],
            end_date_parts[2]
        ).togregorian()

        with transaction.atomic():
            station = FuelStation.objects.create(
                start_date=gregorian_start_date,
                end_date=gregorian_end_date,
            )
        return redirect(reverse('station_detail', args=[station.id]))
    
    return render(request, 'create_station.html'