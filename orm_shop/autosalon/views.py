from django.shortcuts import render, get_object_or_404
from .models import Car, Sale

def cars_list(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    #print(cars.model) # Ошибка: 'QuerySet' object has no attribute 'model'
    #print(cars.model.encode('utf-8').hex())  # Ошибка: 'QuerySet' object has no attribute 'model'
    for car in cars:
        print(car.model)
        print(car.model.encode('utf-8').hex())  # Выводим в шестнадцатеричном формате
    return render(request, 'list.html', context)

def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    context = {'car': car}
    return render(request, 'details.html', context)   

def car_sales(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    sales = Sale.objects.filter(car=car)
    context = {'car': car, 'sales': sales}
    return render(request, 'sales.html', context)