from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth import get_user_model



"""
class cliente(models.Model):
    codigo = models.CharField(max_length=150, null=True, blank=True)
    nombre = models.CharField(max_length=150, null=True, blank=True)
    telefono = models.CharField(max_length=150, null=True, blank=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class  Meta:
        verbose_name = 'clientes'
        verbose_name_plural = 'clientes'

    def __str__(self) :
        return self.nombre
"""

"""lo siguiente es para que el email sea unico"""

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(Group, related_name='custom_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users', blank=True)

    def __str__(self):
        return self.username
    

""" los modelos de los productos"""

class productos(models.Model):
    codigo = models.CharField(max_length=150, primary_key=True)
    nombrep = models.CharField(max_length=150, null=True, blank=True)
    descripcion = models.CharField(max_length=300, null=False, unique=True)
    imagen = models.ImageField( upload_to='imagenes/', verbose_name='imagen', null=True, blank=True)
    costo =  models.IntegerField( null=False)
    cantidad = models.IntegerField(null=False)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.nombrep} -> {self.costo}'


class pedidos(models.Model):
    nombre_pro_pe = models.CharField(max_length=1000)
    total_ped = models.IntegerField( null=False)
    usuario_p = models.CharField(max_length=300)
    correo_usuario = models.CharField(max_length=500)
    create = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre_pro_pe} - {self.usuario_p}"


#esto es para guardar el carrito de el usuario

class Carrito(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    producto = models.ForeignKey(productos, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.producto.nombrep}"