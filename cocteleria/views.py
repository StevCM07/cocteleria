from django.shortcuts import render, redirect
from .models import Carrito
from .models import productos
from .models import pedidos
from .models import CustomUser
from .forms import UserRegisterForm
from django.contrib import messages
from .cart import Cart  
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt



def inicio(request):
    return render(request, 'inicio.html')

def tiendas(request):
    return render(request, 'tiendas.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def productosh(request):
    producto = productos.objects.all()
    return render(request, 'productosh.html', {'productos': producto})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('productosh')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context)

@login_required(login_url='login')
def add_productos(request, productos_codigo):
    cart_instance = Cart(request)  # Cambio en el nombre de la instancia
    producto = productos.objects.get(codigo=productos_codigo)
    cart_instance.add(producto)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def remove_productos(request, productos_codigo):
    cart_instance = Cart(request)  # Cambio en el nombre de la instancia
    producto = productos.objects.get(codigo=productos_codigo)
    cart_instance.remove(producto)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def decrement_productos(request, productos_codigo):
    cart_instance = Cart(request)
    producto = productos.objects.get(codigo=productos_codigo)
    cart_instance.decrement(producto)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def clear_productos(request):
    cart_instance = Cart(request)  # Cambio en el nombre de la instancia
    cart_instance.clear()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def enviar_pedido(request):
    if request.method == 'POST':
        usuario = request.user

        # Obtener los elementos del carrito desde la sesión
        carrito_session = request.session.get('cart', {})
        total_pedido = 0
        nombre_productos = []

        # Calcular el total del pedido sumando los costos de los productos en el carrito
        for key, value in carrito_session.items():
            producto = productos.objects.get(codigo=key)
            total_pedido += producto.costo * value['cantidad']
            nombre_productos.append(producto.nombrep)

        # Crear el objeto de pedido en la base de datos
        pedido = pedidos(
            nombre_pro_pe=', '.join(nombre_productos),
            total_ped=total_pedido,
            usuario_p=usuario.username,
            correo_usuario=usuario.email
        )
        pedido.save()

        # Limpiar el carrito de la sesión
        del request.session['cart']

        # Redireccionar a la página de pedidos en el administrador
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
