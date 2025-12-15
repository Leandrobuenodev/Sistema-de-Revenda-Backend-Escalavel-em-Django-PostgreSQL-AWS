from django import forms
from cars.models import Car


# O ModelForm gera automaticamente campos do formulário e manipulação de dados a partir de um modelo do Django.
class CarModelForm(forms.ModelForm):
        # Meta contém os metadados necessários para que o ModelForm saiba qual modelo do Django usar e quais campos incluir.
    class Meta:
        model = Car
        fields = '__all__' # Instrui o Django a renderizar todos os campos definidos no modelo Car

    # clean é uma função nativa de validação pronta do Django
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 150000:
            self.add_error('value', 'Valor mínimo do carro deve ser de R$ 150.000')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year <= 1975:
            self.add_error('factory_year', 'Carros com ano de fabrica menor ou igual a 1975 não são permitidos')
        return factory_year

    def clean_model_year(self):
        model_year = self.cleaned_data.get('model_year')
        if model_year <= 1975:
            self.add_error('model_year', 'Carros com modelo de fabrica menor ou igual a 1975 não são permitidos')
        return model_year