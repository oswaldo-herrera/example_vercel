from django.forms import ModelForm
from django import forms
from .models import User
from django.utils.translation import gettext_lazy as _

class UserCreationForm(forms.ModelForm):
    # Define los campos que deseas incluir en el formulario
    # email = forms.EmailField()
    email =forms.EmailField(
        label = "Email",
        
        widget=forms.EmailInput(
                attrs={
                    # h-75 rounded-pill ml-1
                    'class':'form-control ',
                    'type': 'email',
                    'placeholder':'usuario@ejemplo.com',
                    
                }
            )        
    )
        
    password1 =forms.CharField(
        max_length=50,
        label = "Contraseña",
        widget=forms.PasswordInput(
                attrs={
                    'class':'form-control ',                    
                    'placeholder':'contraseña',
                    
                }
            )        
    )
    
      
    password2 =forms.CharField(
        max_length=50,
        label = "Contraseña",
        
        widget=forms.PasswordInput(
                attrs={
                    'class':'form-control ',                    
                    'placeholder':'confirmar contraseña...',
                    
                }
            )        
    )
    
    first_name =forms.CharField(
        max_length = 50,
        label = "Usuario",
        
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'nombres...',
                    
                }
            )        
    )
    
    last_name =forms.CharField(
        max_length = 50,
        label = "Usuario",
        
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'primer apellido...',
                    
                }
            )        
    )
   
    second_name =forms.CharField(
        max_length = 50,
        label = "Usuario",
        
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'segundo apellido...',
                    
                }
            )        
    )
    
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name','second_name')
        

class UserChangeForm(forms.ModelForm):
    email =forms.CharField(
        max_length = 50,
        label = "Usuario",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'Usuario...',
                    
                }
            )        
    )
    
    first_name =forms.CharField(
        max_length = 50,
        label = "Nombre",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'Nombre...',
                    
                }
            )        
    )
    
    last_name =forms.CharField(
        max_length = 50,
        label = "Apellido",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'Apellido...',
                    
                }
            )        
    )
    
    second_name =forms.CharField(
        max_length = 50,
        label = "Apellido",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'Apellido...',
                    
                }
            )        
    )
  
    
    telefono_particular =forms.CharField(
        max_length = 50,
        label = "Teléfono particular",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'Teléfono...',
                    
                }
            )        
    )
        
    fecha_nac =forms.DateField(
        required=True,
        widget=forms.DateInput(
                attrs={
                    'class':'form-control ',
                    'type': 'date'
                    
                    
                }
            )        
    )
    
    curp =forms.FileField(
        label = "CURP",
        required=True,
        widget=forms.ClearableFileInput(
                attrs={
                    'accept':'application/pdf',
                    'class':'form-control ',
                    'placeholder':'CURP...',
                    'type': 'file',
                    
                }
            ),        
        help_text=_('Solo se permiten archivos PDF')
    )
    
    documento_ine =forms.FileField(
        label = "INE",
        required=True,
        widget=forms.ClearableFileInput(
                attrs={
                    'accept':'application/pdf',
                    'class':'form-control ',
                    'placeholder':'INE...',
                    'type': 'file',
                    
                }
            ),        
        help_text=_('Solo se permiten archivos PDF')
    )
    
    
    
    comprobante_domicilio =forms.FileField(
        label = "Comprobante domicilio:",
        required=True,
        widget=forms.ClearableFileInput(
                attrs={
                    'accept':'application/pdf',
                    'class':'form-control ',
                    'placeholder':'Comprobante domicilio:...',
                    'type': 'file',
                    
                    
                }
            ),        
        help_text=_('Solo se permiten archivos PDF')
    )
    
    documento_ine_aval =forms.FileField(
        label = "INE:",
        required=True,
        widget=forms.ClearableFileInput(
                attrs={
                    'accept':'application/pdf',
                    'class':'form-control ',
                    'placeholder':'INE:...',
                    'type':'file',
                    
                }
            ),        
        help_text=_('Solo se permiten archivos PDF')
    )
    
    
    comprobante_domicilio_aval =forms.FileField(
        label = "Comprobante domicilio:",
        required=True,
        widget=forms.ClearableFileInput(
                attrs={
                    'accept':'application/pdf',
                    'class':'form-control ',
                    'placeholder':'Comprobante domicilio:...',
                    'type':'file',
                    
                }
            ),        
        help_text=_('Solo se permiten archivos PDF')
    )
    
    curp_aval =forms.FileField(
        label = "CURP:",
        required=True,
        widget=forms.ClearableFileInput(
                attrs={
                    'accept':'application/pdf',
                    'class':'form-control ',
                    'placeholder':'CURP:...',
                    'type':'file',
                    
                }
            ),        
        help_text=_('Solo se permiten archivos PDF')
    )
    
    rfc =forms.CharField(
        max_length = 50,
        label = "RFC",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'RFC...',
                    
                }
            )        
    )
    
    estado_civil =forms.CharField(
        max_length = 50,
        label = "Estado Civil",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'Estado Civil...',
                    
                }
            )        
    )
    
    genero =forms.CharField(
        max_length = 50,
        label = "Genero",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'Genero...',
                    
                }
            )        
    )
    
    nacionalidad =forms.CharField(
        max_length = 50,
        label = "Nacionalidad",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'Nacionalidad...',
                    
                }
            )        
    )
    
    pais =forms.CharField(
        max_length = 50,
        label = "Pais",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'Estado...',
                    
                }
            )        
    )
    
    estado =forms.CharField(
        max_length = 50,
        label = "Estado",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'Estado...',
                    
                }
            )        
    )
    
    celular =forms.CharField(
        max_length = 50,
        label = "Celular",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'Celular...',
                    
                }
            )        
    )
    
    numero_dependientes =forms.CharField(
        max_length = 50,
        label = "Dependientes",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'Dependientes...',
                    
                }
            )        
    )
    
    
    calle_numero =forms.CharField(
        max_length = 50,
        label = "Calle y Numero",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'Calle y numero...',
                    
                }
            )        
    )
    
    colonia =forms.CharField(
        max_length = 50,
        label = "Colonia",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'Colonia...',
                    
                }
            )        
    )
    
    cp =forms.CharField(
        max_length = 50,
        label = "C.P.",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'C.P....',
                    
                }
            )        
    )
    
    ciudad =forms.CharField(
        max_length = 50,
        label = "Ciudad",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'Ciudad...',
                    
                }
            )        
    )
    
    estado_direccion =forms.CharField(
        max_length = 50,
        label = "Estado Direccion",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'Estado Direccion...',
                    
                }
            )        
    )
    
    tipo_vivienda =forms.CharField(
        max_length = 50,
        label = "Tipo de vivienda",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'Tipo de vivienda...',
                    
                }
            )        
    )
    
    
    años_radicando =forms.CharField(
        max_length = 50,
        label = "Años radicando",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'años radicando...',
                    
                }
            )        
    )
    
    conyuge_pareja =forms.CharField(
        max_length = 50,
        label = "Conyuge",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'conyuge...',
                    
                }
            )        
    )
    
    trabajo_conyuge =forms.CharField(
        max_length = 50,
        label = "Trabajo",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'trabajo...',
                    
                }
            )        
    )
    
    antiguedad_laboral_conyuge =forms.CharField(
        max_length = 50,
        label = "Antiguedad laboral",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'antiguedad laboral...',
                    
                }
            )        
    )
    
    telefono_conyuge =forms.CharField(
        max_length = 50,
        label = "Teléfono",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'teléfono...',
                    
                }
            )        
    )
    
    referencia_personal_conyuge_1 =forms.CharField(
        max_length = 50,
        label = "Primer referencia ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'referencia...',
                    
                }
            )        
    )
    
    telefono_ref_conyuge_1 =forms.CharField(
        max_length = 50,
        label = "Teléfono",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'teléfono...',
                    
                }
            )        
    )
    
    referencia_personal_conyuge_2 =forms.CharField(
        max_length = 50,
        label = "Segunda referencia ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'referencia...',
                    
                }
            )        
    )
    
    telefono_ref_conyuge_2 =forms.CharField(
        max_length = 50,
        label = "Primer referencia ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'referencia...',
                    
                }
            )        
    )
    
    nombre_negocio =forms.CharField(
        max_length = 50,
        label = "Nombre del negocio ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'negocio...',
                    
                }
            )        
    )
    
    giro =forms.CharField(
        max_length = 50,
        label = "Giro ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'giro...',
                    
                }
            )        
    )
    
    inmueble =forms.CharField(
        max_length = 50,
        label = "Inmueble ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'inmueble...',
                    
                }
            )        
    )
    
    años_antiguedad =forms.CharField(
        max_length = 50,
        label = "Años de antiguedad ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'antiguedad...',
                    
                }
            )        
    )
    
    calle_numero_negocio =forms.CharField(
        max_length = 50,
        label = "Calle y numero ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'calle...',
                    
                }
            )        
    )
    
    colonia_negocio =forms.CharField(
        max_length = 50,
        label = "Colonia del negocio ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'colonia...',
                    
                }
            )        
    )
    
    cp_negocio =forms.CharField(
        max_length = 50,
        label = "C.P. negocio ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'c.p. ...',
                    
                }
            )        
    )
    
    ciudad_negocio =forms.CharField(
        max_length = 50,
        label = "Ciudad ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'ciudad...',
                    
                }
            )        
    )
    
    estado_negocio =forms.CharField(
        max_length = 50,
        label = "Estado ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'estado...',
                    
                }
            )        
    )
    
    nombre_aval =forms.CharField(
        max_length = 50,
        label = "Nombre ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'nombre...',
                    
                }
            )        
    )
    
    primer_apellido =forms.CharField(
        max_length = 50,
        label = "Primer apellido ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'primer apellido...',
                    
                }
            )        
    )
    
    segundo_apellido =forms.CharField(
        max_length = 50,
        label = "Segundo apellido ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'segundo apellido...',
                    
                }
            )        
    )
    
    
    fecha_nac_aval =forms.DateField(
        required=True,
        widget=forms.DateInput(
                attrs={
                    'class':'form-control ',
                    'type': 'date'
                    
                    
                }
            )        
    )
    
    email_aval =forms.CharField(
        max_length = 50,
        label = "Email ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'email...',
                    
                }
            )        
    )
    
    genero_aval =forms.CharField(
        max_length = 50,
        label = "Genero ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'genero...',
                    
                }
            )        
    )
    
    ciudad_aval =forms.CharField(
        max_length = 50,
        label = "Ciudad ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'ciudad...',
                    
                }
            )        
    )
    
    estado_aval =forms.CharField(
        max_length = 50,
        label = "Estado ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'estado...',
                    
                }
            )        
    )
    
    rfc_aval =forms.CharField(
        max_length = 50,
        label = "RFC ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'rfc...',
                    
                }
            )        
    )
    
    calle_numero_aval =forms.CharField(
        max_length = 50,
        label = "Calle y numero ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'calle y numero...',
                    
                }
            )        
    )
    
    colonia_aval =forms.CharField(
        max_length = 50,
        label = "Colonia ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'colonia...',
                    
                }
            )        
    )
    
    cp_aval =forms.CharField(
        max_length = 50,
        label = "C.P. ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'c.p. ...',
                    
                }
            )        
    )
    
    relacion_titular =forms.CharField(
        max_length = 50,
        label = "Relacion con el titular ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'relacion...',
                    
                }
            )        
    )
    
    tipo_vivienda_aval =forms.CharField(
        max_length = 50,
        label = "Tipo de vivienda ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'vivienda...',
                    
                }
            )        
    )
    
    años_radicando_aval =forms.CharField(
        max_length = 50,
        label = "Años radicando ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'radicando...',
                    
                }
            )        
    )
    
    lugar_trabajo_aval =forms.CharField(
        max_length = 50,
        label = "Lugar de trabajo ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'lugar trabajo...',
                    
                }
            )        
    )
    
    antiguedad_trabajo_aval =forms.CharField(
        max_length = 50,
        label = "Antiguedad de trabajo ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'antiguedad trabajo...',
                    
                }
            )        
    )
    
    celular_aval =forms.CharField(
        max_length = 50,
        label = "Celular ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    'class':'form-control ',
                    'placeholder':'celular...',
                    
                }
            )        
    )
    
    telefono_laboral_aval =forms.CharField(
        max_length = 50,
        label = "Telefono laboral ",
        required=True,
        widget=forms.TextInput(
                attrs={
                    
                    'class':'form-control',
                    'placeholder':'telefono...',
                    
                    
                }
            )        
    )
    
    
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name','second_name','fecha_nac','curp','rfc','estado_civil','genero','nacionalidad','pais','estado','celular','numero_dependientes','telefono_particular','calle_numero','colonia','cp','ciudad','estado_direccion','tipo_vivienda','años_radicando','conyuge_pareja','trabajo_conyuge','antiguedad_laboral_conyuge','telefono_conyuge','referencia_personal_conyuge_1','telefono_ref_conyuge_1','referencia_personal_conyuge_2','telefono_ref_conyuge_2','nombre_negocio','giro','inmueble','años_antiguedad','calle_numero_negocio','colonia_negocio','cp_negocio','ciudad_negocio','estado_negocio','nombre_aval','primer_apellido','segundo_apellido','fecha_nac_aval','curp_aval','genero_aval','ciudad_aval','estado_aval','rfc_aval','calle_numero_aval','colonia_aval','cp_aval','relacion_titular','tipo_vivienda_aval','años_radicando_aval','lugar_trabajo_aval','antiguedad_trabajo_aval','celular_aval','email_aval','telefono_laboral_aval','documento_ine','comprobante_domicilio','documento_ine_aval','comprobante_domicilio_aval')