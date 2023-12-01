from django import forms 
from .models import Productos,Plazo,Simulador



class SimuladorForm(forms.ModelForm):
    
    tipo_credito = forms.ModelChoiceField(
        queryset= Productos.objects.all(),
        label = 'Tipo de crédito',        
        required=False,
        empty_label="Seleccionar",
        initial= 0,
        widget= forms.Select(
            attrs={
                'id':'id_tipo_credito',
                'class':'form-control btn btn-outline-light w-25 mt-2 rounded-pill',
                'placeholder':'Seleccionar',
                
            }
        )
    )
    
    amount = forms.DecimalField(
        label='Monto',
        required=False,
        widget=forms.widgets.NumberInput(
            attrs={
                'id': 'id_amount',
                'class': 'input-range d-none',                
                'type': 'range',
                'onchange':'rangeSlide(this.value)',
                'onmousemove':'rangeSlide(this.value)'
            }
        )
    )
    
    
    # def __init__(self, *args, **kwargs):
    #     super(SimuladorForm, self).__init__(*args, **kwargs)
    #     # Definir las opciones predeterminadas para el campo 'amount'
    #     self.fields['amount'].widget.choices = [('5000', '5000'), ('10000', '10000'), ('15000', '15000')]
    
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     tipo_credito = cleaned_data.get('tipo_credito')
        
    #     if tipo_credito:
    #         if tipo_credito.nombre_credito == 'Credito clasico':
    #             self.fields['amount'].widget.choices = [('5000','5000'),('10000','10000'),('15000','15000')]
    #         elif tipo_credito.nombre_credito == 'Empresarial':
    #             self.fields['amount'].widget.choices = [('20000','20000'),('25000','25000'),('30000','30000')]
    #     return cleaned_data
    
    
                
    
    # amount = forms.DecimalField(
        
    #     label = 'Monto',
    #     required=False,
       
    #     widget= forms.Select(
    #         attrs={
    #             'id': 'id_amount',
    #             'class':'form-control',
    #             'placeholder':'Seleccionar'
    #         }
    #     )
    # )
    

    interest_rate = forms.DecimalField(
            label='Interés',
            required=False,
            widget= forms.NumberInput(
                attrs={
                    'id': 'id_interest_rate',
                    'class':'form-control',
                    
                    
                }
            )
        )
        
    plazo_nombre = forms.ModelChoiceField(
        queryset= Plazo.objects.all(),
        label = 'Tipo de plazo',
        required=False,
        empty_label='Seleccionar',
        initial= 0,
        widget= forms.Select(
            attrs={
                'id':'id_plazo_nombre',
                'class':'form-control btn btn-outline-light w-25 mt-1 rounded-pill',
                'placeholder':'Tipo de plazo'
            }
        )
    )

    term = forms.IntegerField(
        
        label = 'Pagos',
        required=False,
        widget= forms.widgets.NumberInput(
            attrs={
                'id': 'id_term',
                'class':'input-range d-none',
                'type':'range',
                'placeholder':'12,14,16...',
                'onchange':'rangeSlideTerm(this.value)',
                'onmousemove':'rangeSlideTerm(this.value)'
            }
        )
    )
        
    class Meta:
        model = Simulador
        fields = ['tipo_credito','amount','interest_rate','plazo_nombre', 'term']


class ProductosForm(forms.ModelForm):
    nombre_credito =forms.CharField(
        max_length = 50,
        label = "Credito",
        required=False,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'Credito...',
                    
                }
            )        
    )
    
    class Meta:
        model = Productos
        fields = ['nombre_credito']
        
        
        
class PlazoPagoForm(forms.ModelForm):
    
    plazo_tiempo = forms.CharField(
       max_length= 50,
        label='Plazo',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'semanal,quincenal o mensual...',
            }
        )
    )
    
    interes_credito =forms.DecimalField(        
        label = "Interes",
        required=False,
        widget=forms.NumberInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'Interes...',
                    
                }
            )        
    )
    
    class Meta:
        model = Plazo 
        fields = ['plazo_tiempo','interes_credito']
        
        


    
