from django import forms
from cars.models import Brand, Car

#ARQUIVO DE FORMS ODE CONSENTRARÃO TODOS OS FORMULÁRIOS, FOI FEITA A INPORTAÇÃO ACIMA

#ABAIXO TEMOS O FORM QUE APARECERÁ PARA O USUARIOS. ESSA É A FORMA MAIS "DIFICIL"
"""class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all()) 
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

    #CRIAMOS UMA FUNÇÃO PARA SALVAR OS DADOS QUE O USUARIO ESTÁ ENVIADO.
    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo']
        )
        car.save()
        return car"""

#ABAIXO TEMOS O FORM QUE APARECERÁ PARA O USUARIOS, MAS DESSA VEZ ESTAMOS UTILIZANDO O FORMS.MODELFORM
class CarModelFom(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data['value']
        if value < 20000:
            self.add_error ('O valor não deve ser menor que R$ 20.000')
        return value


    
