from django.urls import path
from . import views

urlpatterns = [
    path('listar_productos/', views.listar_productos, name='listar_productos'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
]
