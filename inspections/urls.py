from django.urls import path
from .views import create_station, add_tanks, add_nozzles, station_detail, render_pdf_view


urlpatterns = [
    path('', create_station, name='create_station'),
    path('station/<int:station_id>/add_tanks/', add_tanks, name='add_tanks'),
    path('station/<int:station_id>/add_nozzles/', add_nozzles, name='add_nozzles'),
    path('station/<int:station_id>/', station_detail, name='station_detail'),
    path('station/<int:station_id>/pdf/', render_pdf_view, name='render_pdf'),
    
]
