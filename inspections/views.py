# reports/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FuelStation, Tank, Nozzle
from django.template.loader import get_template
from xhtml2pdf import pisa

def create_station(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gasoline_tanks = int(request.POST.get('gasoline_tanks'))
        gasoline_nozzles = int(request.POST.get('gasoline_nozzles'))
        gas_nozzles = int(request.POST.get('gas_nozzles'))


        gas_tanks = int(request.POST.get('gas_tanks'))
        gasoline_beginning = float(request.POST.get('gasoline_beginning'))
        gas_beginning = float(request.POST.get('gas_beginning'))
        gasoline_received = float(request.POST.get('gasoline_received'))
        gas_received = float(request.POST.get('gas_received'))
        electronic_gasoline_sales = float(request.POST.get('electronic_gasoline_sales'))
        electronic_gas_sales = float(request.POST.get('electronic_gas_sales'))
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        station = FuelStation.objects.create(
            name=name,
            gasoline_tanks=gasoline_tanks,
            gas_tanks=gas_tanks,
            gasoline_nozzles=gasoline_nozzles,
            gas_nozzles=gas_nozzles,
            gasoline_beginning=gasoline_beginning,
            gas_beginning=gas_beginning,
            gasoline_received=gasoline_received,
            gas_received=gas_received,
            electronic_gasoline_sales=electronic_gasoline_sales,
            electronic_gas_sales=electronic_gas_sales,
            start_date=start_date,
            end_date=end_date
        )
        return redirect('add_tanks', station_id=station.id)
    return render(request, 'create_station.html')

def add_tanks(request, station_id):
    station = FuelStation.objects.get(id=station_id)
    if request.method == 'POST':
        for i in range(station.gasoline_tanks):
            amount = float(request.POST.get(f'gasoline_tank_{i}'))
            Tank.objects.create(station=station, type='gasoline', amount=amount)
        for i in range(station.gas_tanks):
            amount = float(request.POST.get(f'gas_tank_{i}'))
            Tank.objects.create(station=station, type='gas', amount=amount)
        return redirect('add_nozzles', station_id=station.id)
    return render(request, 'add_tanks.html', {'station': station})

def add_nozzles(request, station_id):
    station = FuelStation.objects.get(id=station_id)
    if request.method == 'POST':
        for i in range(station.gasoline_nozzles):
            start_totalizer = float(request.POST.get(f'gasoline_nozzle_start_totalizer_{i}'))
            end_totalizer = float(request.POST.get(f'gasoline_nozzle_end_totalizer_{i}'))
            Nozzle.objects.create(station=station, type='gasoline', start_totalizer=start_totalizer, end_totalizer=end_totalizer)
        for i in range(station.gas_nozzles):
            start_totalizer = float(request.POST.get(f'gas_nozzle_start_totalizer_{i}'))
            end_totalizer = float(request.POST.get(f'gas_nozzle_end_totalizer_{i}'))
            Nozzle.objects.create(station=station, type='gas', start_totalizer=start_totalizer, end_totalizer=end_totalizer)
        return redirect('station_detail', station_id=station.id)
    return render(request, 'add_nozzles.html', {'station': station})

def station_detail(request, station_id):
    station = FuelStation.objects.get(id=station_id)
    nozzles = Nozzle.objects.filter(station=station)
    tanks = Tank.objects.filter(station=station)

    gasoline_mechanical_sales = sum(n.mechanical_sales() for n in nozzles if n.type == 'gasoline')
    gas_mechanical_sales = sum(n.mechanical_sales() for n in nozzles if n.type == 'gas')

    gasoline_end_inventory = sum(t.amount for t in tanks if t.type == 'gasoline')
    gas_end_inventory = sum(t.amount for t in tanks if t.type == 'gas')

    total_gasoline_inventory = station.gasoline_beginning + station.gasoline_received
    total_gas_inventory = station.gas_beginning + station.gas_received

    gasoline_outflow = total_gasoline_inventory - gasoline_end_inventory
    gas_outflow = total_gas_inventory - gas_end_inventory

    gasoline_after_sales = total_gasoline_inventory - gasoline_mechanical_sales
    gas_after_sales = total_gas_inventory - gas_mechanical_sales

    gasoline_difference = gasoline_end_inventory - gasoline_after_sales
    gas_difference = gas_end_inventory - gas_after_sales

    gasoline_status = 'کسری' if gasoline_difference > gasoline_end_inventory else 'سرک'
    gas_status = 'کسری' if gas_difference > gas_end_inventory else 'سرک'

    context = {
        'station': station,
        'nozzles': nozzles,
        'tanks': tanks,
        'gasoline_mechanical_sales': gasoline_mechanical_sales,
        'gas_mechanical_sales': gas_mechanical_sales,
        'gasoline_end_inventory': gasoline_end_inventory,
        'gas_end_inventory': gas_end_inventory,
        'total_gasoline_inventory': total_gasoline_inventory,
        'total_gas_inventory': total_gas_inventory,
        'gasoline_outflow': gasoline_outflow,
        'gas_outflow': gas_outflow,
        'gasoline_after_sales': gasoline_after_sales,
        'gas_after_sales': gas_after_sales,
        'gasoline_difference': gasoline_difference,
        'gas_difference': gas_difference,
        'gasoline_status': gasoline_status,
        'gas_status': gas_status,
    }

    return render(request, 'station_detail.html', context)

def render_pdf_view(request, station_id):
    station = FuelStation.objects.get(id=station_id)
    template_path = 'pdf_template.html'
    context = station_detail(request, station_id).context_data

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
