from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelFom

def cars_viwe(request):
    cars = Car.objects.all().order_by('brand')  
    search = request.GET.get('search')
    
    #cars = Car.objects.all() AQUI PEGARIA TODAS AS INFORMAÇÕES UTILIZANDO A FUNÇÃO >>ALL<<
    if search:
        cars = cars.filter(model__icontains = search) #AQUI ESTOU FAZENDO UM CONSULTA UTILIZANDO FILTRO
    return render(request, 'cars.html', {'cars':cars})

    """NO CÓDIGO ACIMA O USUARIO VAI BATER NA URL CARS, O SISTEMA VAI MOSTRAR A LISTA COMPLETA DE TODOS OS VEICULOS
    MAS CASO O USUARIO PASSE UM FILTRO O SISTEMA MOSTRARÁ A INFORMAÇÃO FILTRADAS
    """

def new_car_view(request):
    #CAPTURANDO OS DADOS DO FORM, QUE O USUARIO PREENCHEU
    if request.method == 'POST':
        new_car_form = CarModelFom(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            """new_car_form = CarForm()"""
            return redirect('cars_list')
    else:

        new_car_form = CarModelFom()
    return render(request, 'new_car.html', {'new_car_form': new_car_form})