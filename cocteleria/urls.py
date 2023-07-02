from django.urls import path
from .import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productosh/', views.productosh, name='productosh'),
    path('tiendas/', views.tiendas, name='tiendas'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('add/<str:productos_codigo>/', views.add_productos, name='add'),
    path('remove/<str:productos_codigo>/', views.remove_productos, name='remove'),
    path('decrement/<str:productos_codigo>/', views.decrement_productos, name='decrement'),
    path('clear/', views.clear_productos, name='clear'),
    path('enviar_pedido/', views.enviar_pedido, name='enviar_pedido'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
