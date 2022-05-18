from django.contrib import admin
from apps.ventas.models import Venta, VehiculoVenta

class MembershipInline(admin.TabularInline):
    model = VehiculoVenta
    extra = 1

class VentaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'valorTotal', 'tipoPago', 'user')
    #ordering = ('fecha', 'user')
    #search_fields = ('fecha', 'user')
    #list_filter = ('fecha', 'valorTotal', 'tipoPago', 'user')
    inlines = (MembershipInline,)

admin.site.register(Venta, VentaAdmin)
