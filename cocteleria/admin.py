from django.contrib import admin
from .models import  productos
from .models import CustomUser
from .models import pedidos
from .models import Carrito

admin.site.register(CustomUser)

class pedidosAdmin(admin.ModelAdmin):
    list_display = ['nombre_pro_pe', 'total_ped', 'usuario_p', 'correo_usuario']
    list_filter = ['usuario_p']
    search_fields = ['usuario_p']
    # Resto de opciones de personalización...

admin.site.register(pedidos, pedidosAdmin)

# Register your models here.


class productosadmin(admin.ModelAdmin):
    list_display = ('nombrep','codigo', 'descripcion', 'imagen', 'costo' ,'cantidad')
    search_fields = ['descripcion']
    readonly_fields = ('create', 'update')
    filter_horizontal = ()
    list_filter =()
    fields = ()

admin.site.register(productos, productosadmin)