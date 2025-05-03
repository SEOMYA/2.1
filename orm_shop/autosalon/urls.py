from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.cars_list, name='cars_list'),
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
    path('cars/<int:car_id>/sales/', views.car_sales, name='car_sales'),
]