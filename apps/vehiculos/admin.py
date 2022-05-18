from django.contrib import admin
from apps.vehiculos.models import Vehiculos, Tipovehiculo, Marca

# Register your models here.

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'color', 'placa', 'motor', 'marca', 'tipovehiculo')
    ordering = ('modelo', 'color', 'placa', 'motor', 'marca', 'tipovehiculo')
    search_fields = ('modelo', 'marca__nombre')
    list_filter = ('modelo', 'marca__nombre', 'tipovehiculo__nombre')

admin.site.register(Tipovehiculo)
admin.site.register(Marca)
admin.site.register(Vehiculos)
