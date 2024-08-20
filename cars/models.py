from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
   

# CREATING A TABLE OF CARS
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name= 'car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    km = models.FloatField(blank=False, null=False, verbose_name="KM")
    photo = models.ImageField(upload_to='cars/', blank=False, null=False)
    bio = models.TextField(blank=True, null=True, name="description")

    def __str__(self):
        return self.model
    
class CarInvetory(models.Model):
    cars_count = models.IntegerField(verbose_name="Carros em Estoque", blank= True, null= True)
    cars_value = models.FloatField(verbose_name="Valor Total em do Estoque", blank= True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'