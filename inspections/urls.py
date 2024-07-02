from django.urls import path
from .views import home, create_station, station_detail, generate_pdf, latest_data


urlpatterns = [
    path('', home, name='home'),
    path('station/create/', create_station, name='create_station'),
    # path('station/<int:station_id>/add_tanks/', add_tanks, name='add_tanks'),
    # path('station/<int:station_id>/add_nozzles/', add_nozzles, name='add_nozzles'),
    path('station/<int:station_id>/', station_detail, name='station_detail'),
    path('generate_pdf/<int:station_id>/', generate_pdf, name='generate_pdf'),
    path('station/<int:station_id>/latest/', latest_data, name='latest_data'),

    
]
