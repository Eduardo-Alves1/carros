from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelFom
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class CarLitView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains = search)
            #AQUI ESTOU FAZENDO UM CONSULTA UTILIZANDO FILTRO
        return cars

        #cars = Car.objects.all() AQUI PEGARIA TODAS AS INFORMAÇ��ES UTILIZANDO A FUNÇÃO >>ALL<<

class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelFom
    template_name = 'new_car.html'
    success_url = '/cars/'


class CarDatailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelFom
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'