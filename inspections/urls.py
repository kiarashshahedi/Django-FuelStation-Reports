from django.urls import path
from .views import home, create_station, station_detail, render_pdf_view, latest_data


urlpatterns = [
    path('', home, name='home'),
    path('station/create/', create_station, name='create_station'),
    # path('station/<int:station_id>/add_tanks/', add_tanks, name='add_tanks'),
    # path('station/<int:station_id>/add_nozzles/', add_nozzles, name='add_nozzles'),
    path('station/<int:station_id>/', station_detail, name='station_detail'),
    path('station/<int:station_id>/pdf/', render_pdf_view, name='render_pdf'),
    path('station/<int:station_id>/latest/', latest_data, name='latest_data'),

    
]
