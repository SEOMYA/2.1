from django.shortcuts import render, get_object_or_404
from .models import Car, Sale

def cars_list(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'autosalon/list.html', context)

def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    context = {'car': car}
    return render(request, 'autosalon/details.html', context)   

def car_sales(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    sales = Sale.objects.filter(car=car)
    context = {'car': car, 'sales': sales}
    return render(request, 'autosalon/sales.html', context)