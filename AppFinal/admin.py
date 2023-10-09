from django.contrib import admin
from .models import Tipo_Servicio, Cliente, Lugar_Evento, Trabajos_entregar, Avatar

# Register your models here.
admin.site.register(Tipo_Servicio)
admin.site.register(Cliente)
admin.site.register(Lugar_Evento)
admin.site.register(Trabajos_entregar)
admin.site.register(Avatar)