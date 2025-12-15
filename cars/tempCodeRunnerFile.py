from django.shortcuts import render
from cars.models import Car

# func() Views | URL /cars busca na -->Func() Views a func() cars_view(resquest)
def cars_view(request):
    cars = Car.objects.all()
    print(cars)

    return render(
        request,
        'cars.html',)
