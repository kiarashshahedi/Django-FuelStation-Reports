from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import FuelStation, Tank, Nozzle
from django.db import transaction
from django.urls import reverse
from weasyprint import HTML
from django.template.loader import render_to_string
import jdatetime




def home(request):
    return render(request, 'home.html')

def create_station(request):
    if request.method == 'POST':
        print(request.POST)  # Debugging: print all POST data

        try:
            name = request.POST.get('name')
            gasoline_tanks = int(request.POST.get('gasoline_tanks', '0') or '0')
            gasoline_nozzles = int(request.POST.get('gasoline_nozzles', '0') or '0')
            gas_nozzles = int(request.POST.get('gas_nozzles', '0') or '0')
            gas_tanks = int(request.POST.get('gas_tanks', '0') or '0')
            gasoline_beginning = float(request.POST.get('gasoline_beginning', '0') or '0')
            gas_beginning = float(request.POST.get('gas_beginning', '0') or '0')
            gasoline_received = float(request.POST.get('gasoline_received', '0') or '0')
            gas_received = float(request.POST.get('gas_received', '0') or '0')
            electronic_gasoline_sales = float(request.POST.get('electronic_gasoline_sales', '0') or '0')
            electronic_gas_sales = float(request.POST.get('electronic_gas_sales', '0') or '0')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            controller = request.POST.get('controller')

            with transaction.atomic():
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
                    end_date=end_date,
                    controller=controller
                )

                for i in range(1, gasoline_tanks + 1):
                    amount = float(request.POST.get(f'gasoline_tank_{i}', '0') or '0')
                    print(f'Gasoline Tank {i} amount: {amount}')  # Debug

                    Tank.objects.create(station=station, type='gasoline', amount=amount)

                for i in range(1, gas_tanks + 1):
                    amount = float(request.POST.get(f'gas_tank_{i}', '0') or '0')
                    print(f'Gas Tank {i} amount: {amount}')  # Debug
                    Tank.objects.create(station=station, type='gas', amount=amount)

                for i in range(gasoline_nozzles):
                    start_totalizer = float(request.POST.get(f'gasoline_nozzle_start_totalizer_{i}', '0') or '0')
                    end_totalizer = float(request.POST.get(f'gasoline_nozzle_end_totalizer_{i}', '0') or '0')
                    Nozzle.objects.create(station=station, type='gasoline', start_totalizer=start_totalizer, end_totalizer=end_totalizer)

                for i in range(gas_nozzles):
                    start_totalizer = float(request.POST.get(f'gas_nozzle_start_totalizer_{i}', '0') or '0')
                    end_totalizer = float(request.POST.get(f'gas_nozzle_end_totalizer_{i}', '0') or '0')
                    Nozzle.objects.create(station=station, type='gas', start_totalizer=start_totalizer, end_totalizer=end_totalizer)

            return redirect(reverse('station_detail', args=[station.id]))

        except ValueError as e:
            print(f"ValueError: {e}")  # Debugging: print the error message

    return render(request, 'create_station.html')

# def add_tanks(request, station_id):
#     station = FuelStation.objects.get(id=station_id)
#     if request.method == 'POST':
#         for i in range(station.gasoline_tanks):
#             amount = float(request.POST.get(f'gasoline_tank_{i}'))
#             Tank.objects.create(station=station, type='gasoline', amount=amount)
#         for i in range(station.gas_tanks):
#             amount = float(request.POST.get(f'gas_tank_{i}'))
#             Tank.objects.create(station=station, type='gas', amount=amount)
#         return redirect('add_nozzles', station_id=station.id)
#     return render(request, 'add_tanks.html', {'station': station})

# def add_nozzles(request, station_id):
#     station = FuelStation.objects.get(id=station_id)
        
#     if request.method == 'POST':
#         for i in range(station.gasoline_nozzles):
#             start_totalizer = float(request.POST.get(f'gasoline_nozzle_start_totalizer_{i}'))
#             end_totalizer = float(request.POST.get(f'gasoline_nozzle_end_totalizer_{i}'))
#             Nozzle.objects.create(station=station, type='gasoline', start_totalizer=start_totalizer, end_totalizer=end_totalizer)
#         for i in range(station.gas_nozzles):
#             start_totalizer = float(request.POST.get(f'gas_nozzle_start_totalizer_{i}'))
#             end_totalizer = float(request.POST.get(f'gas_nozzle_end_totalizer_{i}'))
#             Nozzle.objects.create(station=station, type='gas', start_totalizer=start_totalizer, end_totalizer=end_totalizer)
#         return redirect('station_detail', station_id=station.id)
#     return render(request, 'add_nozzles.html', {'station': station})

def station_detail(request, station_id):
    station = get_object_or_404(FuelStation, id=station_id)
    
    gasoline_nozzles = Nozzle.objects.filter(station=station, type='gasoline')
    gas_nozzles = Nozzle.objects.filter(station=station, type='gas')

    # Prepare nozzle sales data
    gasoline_nozzle_sales = []
    for nozzle in gasoline_nozzles:
        each_nozzle_sale = nozzle.end_totalizer - nozzle.start_totalizer
        gasoline_nozzle_sales.append({
            'nozzle': nozzle,
            'sale': each_nozzle_sale
        })

    gas_nozzle_sales = []
    for nozzle in gas_nozzles:
        each_nozzle_sale = nozzle.end_totalizer - nozzle.start_totalizer
        gas_nozzle_sales.append({
            'nozzle': nozzle,
            'sale': each_nozzle_sale
        })
        
        
        
    gasoline_tanks = Tank.objects.filter(station=station, type='gasoline')
    gas_tanks = Tank.objects.filter(station=station, type='gas')

    print(f"Gasoline tanks: {gasoline_tanks}")
    print(f"Gas tanks: {gas_tanks}")


    # FOROSH MEKANIKI NAZEL HA
    gasoline_mechanical_sales = station.gasoline_mechanical_sales()
    gas_mechanical_sales = station.gas_mechanical_sales()

    # JAME HAMEYE MAKHAZEN
    gasoline_end_inventory = station.total_tank_amount()  
    gas_end_inventory = station.total_gs_tank_amount()  
    
    # EBTEDA DORE + RESIDE = 0+100000
    total_gasoline_inventory = station.gasoline_beginning + station.gasoline_received
    total_gas_inventory = station.gas_beginning + station.gas_received

    # 100000 - MOJODI MAKHAZEN
    gasoline_outflow = total_gasoline_inventory - gasoline_end_inventory
    gas_outflow = total_gas_inventory - gas_end_inventory

    # MEKANIKI - KHAREJ SHODE
    gasoline_difference = gasoline_mechanical_sales  -  gasoline_outflow 
    gas_difference = gas_mechanical_sales - gas_outflow




    # AGE MOSBAT BOD SARAK AGE MANFI BOD KASRI
    gasoline_status = 'کسری' if gasoline_difference < 0 else 'سرک'
    gas_status = 'کسری' if gas_difference < 0 else 'سرک'
    
    # MEKANIKI NAZEL HA * 0.0045 - TAFAVOT FOROSH VA MOJODI(RESIDE)
    qire_mojaz = (gasoline_mechanical_sales * 0.0045) - gasoline_difference
    
    # TAFAVOT ELECTRONIKI VA MEKANIKI
    electronic_mechanical_discrepancy = station.electronic_gasoline_sales - gasoline_mechanical_sales
    electronic_mechanical_discrepancy_gas = station.electronic_gas_sales - gas_mechanical_sales

    # MEQDAR TOTALIZER HAR NOZEL 
    
    

    context = {
        'station': station,
        'gasoline_nozzles': gasoline_nozzles,
        'gas_nozzles': gas_nozzles,
        'gasoline_nozzle_sales': gasoline_nozzle_sales,
        'gas_nozzle_sales': gas_nozzle_sales,
        
        'gasoline_tanks': gasoline_tanks,
        'gas_tanks': gas_tanks,        
        'gasoline_mechanical_sales': gasoline_mechanical_sales,
        'gas_mechanical_sales': gas_mechanical_sales,
        'gasoline_end_inventory': gasoline_end_inventory,
        'gas_end_inventory': gas_end_inventory,
        'total_gasoline_inventory': total_gasoline_inventory,
        'total_gas_inventory': total_gas_inventory,
        'gasoline_outflow': gasoline_outflow,
        'gas_outflow': gas_outflow,
        # 'gasoline_after_sales': gasoline_after_sales,
        # 'gas_after_sales': gas_after_sales,
        'gasoline_difference': gasoline_difference,
        'gas_difference': gas_difference,
        'gasoline_status': gasoline_status,
        'gas_status': gas_status,
        'qire_mojaz': qire_mojaz,
        'electronic_mechanical_discrepancy': electronic_mechanical_discrepancy,
        'electronic_mechanical_discrepancy_gas': electronic_mechanical_discrepancy_gas,
    }

    return render(request, 'station_detail.html', context)

def get_station_context(station_id):
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

    gasoline_difference = gasoline_after_sales - gasoline_end_inventory
    gas_difference = gas_after_sales - gas_end_inventory

    gasoline_status = 'کسری' if gasoline_difference > 0 else 'سرک'
    gas_status = 'کسری' if gas_difference > 0 else 'سرک'

    qire_mojaz = gasoline_mechanical_sales * 0.0045 - gasoline_difference
    electronic_mechanical_discrepancy = station.electronic_gasoline_sales - gasoline_mechanical_sales
    electronic_mechanical_discrepancy_gas = station.electronic_gas_sales - gas_mechanical_sales

    
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
        'qire_mojaz' : qire_mojaz,
        'electronic_mechanical_discrepancy': electronic_mechanical_discrepancy,
        'electronic_mechanical_discrepancy_gas': electronic_mechanical_discrepancy_gas

    }

    return context

def generate_pdf(request, station_id):
    context = get_station_context(station_id)
    html_string = render_to_string('pdf_template.html', context)
    html = HTML(string=html_string)
    pdf = html.write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="station.pdf"'
    return response

def latest_data(request, station_id):
    station = get_object_or_404(FuelStation, id=station_id)
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

    gasoline_difference = gasoline_after_sales - gasoline_end_inventory
    gas_difference = gas_after_sales - gas_end_inventory

    gasoline_status = 'کسری' if gasoline_difference > 0 else 'سرک'
    gas_status = 'کسری' if gas_difference > 0 else 'سرک'
    
    qire_mojaz = gasoline_mechanical_sales * 0.0045 - gasoline_difference
    electronic_mechanical_discrepancy = station.electronic_gasoline_sales - gasoline_mechanical_sales

    qire_mojaz = gasoline_mechanical_sales * 0.0045 - gasoline_difference
    electronic_mechanical_discrepancy = station.electronic_gasoline_sales - gasoline_mechanical_sales
    electronic_mechanical_discrepancy_gas = station.electronic_gas_sales - gas_mechanical_sales
    
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
        'qire_mojaz' : qire_mojaz,
        'electronic_mechanical_discrepancy': electronic_mechanical_discrepancy,
        'electronic_mechanical_discrepancy_gas': electronic_mechanical_discrepancy_gas
    }

    return render(request, 'latest_data.html', context)