from .models import *

class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            self.session["cart"] = {}
            self.cart = self.session["cart"]
        else:
            self.cart = cart

    def add(self, productos):
        codigo = str(productos.codigo)
        if codigo not in self.cart.keys():
            self.cart[codigo] = {
                "productos_codigo": productos.codigo,
                "nombrep": productos.nombrep,
                "cantidad": 1,
                "costo": productos.costo,
                "imagen": productos.imagen.url,
            }
        else:
            self.cart[codigo]["cantidad"] += 1
            self.cart[codigo]["costo"] += productos.costo
        self.save()

    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def remove(self, productos):
        codigo = str(productos.codigo)
        if codigo in self.cart:
            del self.cart[codigo]
            self.save()

    def decrement(self, productos):
        codigo = str(productos.codigo)
        if codigo in self.cart.keys():
            self.cart[codigo]["cantidad"] -= 1
            self.cart[codigo]["costo"] -= productos.costo
            if self.cart[codigo]["cantidad"] <= 0: self.remove(productos)
            self.save()

    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True
