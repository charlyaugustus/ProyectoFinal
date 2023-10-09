from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tipo_Servicio(models.Model):
    nombre = models.CharField(max_length=40)
    evento = models.CharField(max_length=40)
    email = models.EmailField()
    tipo_servicio = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
   

    def __str__(self) -> str:
       
            return f'{self.nombre} - {self.evento} - {self.email} - {self.tipo_servicio} - {self.telefono}'
        
        

class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=40)
    email= models.EmailField()
    tipo_servicio = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
    
    def __str__(self) -> str:
        return f'{self.nombre} - {self.apellido} - {self.email} - {self.tipo_servicio} - {self.telefono}'

class Lugar_Evento(models.Model):
    lugar = models.CharField(max_length=40)
    localidad = models.CharField(max_length=40)
    email = models.EmailField()
    salon = models.CharField(max_length=40)
    
    
    def __str__(self) -> str:
        return f'{self.lugar} - {self.localidad} - {self.email} - {self.salon}'
    
class Trabajos_entregar(models.Model):
    trabajo = models.CharField(max_length=40)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
    link = models.CharField(max_length=256, null=True)
    email = models.EmailField()
    
    def __str__(self) -> str:
        return f'{self.trabajo} - {self.fecha_entrega} - {self.entregado} - {self.link} - {self.email}'

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.user} - {self.imagen}'