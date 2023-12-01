from django.db import models

# Create your models here.

class Productos(models.Model):
    nombre_credito = models.CharField(max_length=100,blank=True,null=True)
    
    def __str__(self):
        return str(self.nombre_credito) 

class Plazo(models.Model):    
    plazo_tiempo = models.CharField(max_length=100,blank=True,null=True) 
    interes_credito = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    

    class Meta:
        verbose_name = 'Plazo'
        verbose_name_plural = 'Plazos'
       

    def __str__(self):
        return str(self.plazo_tiempo) + ' ID:  ' + str(self.id) 



class Simulador(models.Model):
    tipo_credito = models.ForeignKey(Productos, on_delete=models.CASCADE,related_name='tipo_credito',null=True,blank=True)
    plazo_nombre = models.ForeignKey(Plazo,on_delete=models.CASCADE,related_name='nombre_plazo',null=True,blank=True)
    term = models.IntegerField(null=True,blank=True)
    amount = models.IntegerField(null=True,blank=True) 
    interest_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Simulador'
        verbose_name_plural = 'Simuladores'
    
    def __str__(self):
        return str(self.tipo_credito)