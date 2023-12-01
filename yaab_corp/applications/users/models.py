from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    # *************datos personales ***********
    email = models.EmailField(_('enmail adrees'),unique=True)
    username = models.CharField(max_length=150, unique=False, blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    second_name = models.CharField(max_length=30,blank=True,null=True)
    fecha_nac = models.DateField(null=True,blank=True)
     # curp = models.CharField(max_length=30,blank=True,null=True)
    curp = models.FileField(upload_to='users/',blank=True,null=True)
    rfc = models.CharField(max_length=30,blank=True,null=True)
    estado_civil = models.CharField(max_length=30,blank=True,null=True)
    genero = models.CharField(max_length=100,blank=True,null=True)
    nacionalidad = models.CharField(max_length=100,blank=True,null=True)
    pais = models.CharField(max_length=100,blank=True,null=True)
    estado = models.CharField(max_length=100,blank=True,null=True)
    celular = models.CharField(max_length=100,blank=True,null=True)
    numero_dependientes = models.CharField(max_length=100,blank=True,null=True)
    telefono_particular = models.CharField(max_length=100,blank=True,null=True)
    documento_ine = models.FileField(upload_to='users/',blank=True,null=True)
     # *************datos personales ***********
     
      # *************direccion ***********
    calle_numero = models.CharField(max_length=100,blank=True,null=True)
    colonia = models.CharField(max_length=100,blank=True,null=True)
    cp = models.CharField(max_length=100,blank=True,null=True)
    ciudad = models.CharField(max_length=100,blank=True,null=True)
    estado_direccion = models.CharField(max_length=100,blank=True,null=True)
    tipo_vivienda = models.CharField(max_length=100,blank=True,null=True)
    años_radicando = models.CharField(max_length=100,blank=True,null=True)
    comprobante_domicilio = models.FileField(upload_to='users/',blank=True,null=True)
    # *************direccion ***********
    
     # *************referencias ***********      
    conyuge_pareja = models.CharField(max_length=100,blank=True,null=True)
    trabajo_conyuge = models.CharField(max_length=100,blank=True,null=True)
    antiguedad_laboral_conyuge = models.CharField(max_length=100,blank=True,null=True)
    telefono_conyuge = models.CharField(max_length=100,blank=True,null=True)
    referencia_personal_conyuge_1 = models.CharField(max_length=100,blank=True,null=True)
    telefono_ref_conyuge_1 = models.CharField(max_length=100,blank=True,null=True)
    referencia_personal_conyuge_2 = models.CharField(max_length=100,blank=True,null=True)
    telefono_ref_conyuge_2 = models.CharField(max_length=100,blank=True,null=True)
       # *************referencias ***********   
       
        # *************datos del comercio *********** 
    nombre_negocio = models.CharField(max_length=100,blank=True,null=True)
    giro = models.CharField(max_length=100,blank=True,null=True)
    inmueble = models.CharField(max_length=100,blank=True,null=True)
    años_antiguedad = models.CharField(max_length=100,blank=True,null=True)
    calle_numero_negocio = models.CharField(max_length=100,blank=True,null=True)
    colonia_negocio = models.CharField(max_length=100,blank=True,null=True)
    cp_negocio = models.CharField(max_length=100,blank=True,null=True)
    ciudad_negocio = models.CharField(max_length=100,blank=True,null=True)
    estado_negocio = models.CharField(max_length=100,blank=True,null=True)
    # *************datos del comercio *********** 
    
    # ************* datos aval *********** 
    
    nombre_aval = models.CharField(max_length=100,blank=True,null=True)
    primer_apellido = models.CharField(max_length=100,blank=True,null=True)
    segundo_apellido = models.CharField(max_length=100,blank=True,null=True)
    fecha_nac_aval = models.DateField(null=True,blank=True)
    curp_aval = models.FileField(upload_to='users/',blank=True,null=True)
    # curp_aval = models.CharField(max_length=100,blank=True,null=True) 
    genero_aval = models.CharField(max_length=100,blank=True,null=True)
    ciudad_aval = models.CharField(max_length=100,blank=True,null=True)
    estado_aval = models.CharField(max_length=100,blank=True,null=True)
    rfc_aval = models.CharField(max_length=100,blank=True,null=True)
    calle_numero_aval = models.CharField(max_length=100,blank=True,null=True)
    colonia_aval = models.CharField(max_length=100,blank=True,null=True)
    cp_aval = models.CharField(max_length=100,blank=True,null=True)
    relacion_titular = models.CharField(max_length=100,blank=True,null=True)
    tipo_vivienda_aval = models.CharField(max_length=100,blank=True,null=True)
    años_radicando_aval = models.CharField(max_length=100,blank=True,null=True)
    lugar_trabajo_aval = models.CharField(max_length=100,blank=True,null=True)
    antiguedad_trabajo_aval = models.CharField(max_length=100,blank=True,null=True)
    celular_aval = models.CharField(max_length=100,blank=True,null=True)
    email_aval = models.CharField(max_length=100,blank=True,null=True)
    telefono_laboral_aval = models.CharField(max_length=100,blank=True,null=True)
    documento_ine_aval = models.FileField(upload_to='users/',blank=True,null=True)
    comprobante_domicilio_aval = models.FileField(upload_to='users/',blank=True,null=True)
    
    # ************* datos aval *********** 
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email
    

