from django.urls import path
from .views import home, create_station, station_detail, generate_pdf


urlpatterns = [
    path('', home, name='home'),
    path('station/create/', create_station, name='create_station'),
    path('station/<int:station_id>/', station_detail, name='station_detail'),
    path('generate_pdf/<int:station_id>/', generate_pdf, name='generate_pdf'),
]
