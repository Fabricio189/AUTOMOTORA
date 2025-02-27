from django.urls import path
from .views import home, galeria, formulario, listar_automoviles, eliminar_automovil, modificar_automovil

#Importamos todo lo q esta en los view
urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('formulario/', formulario, name="formulario"),
    path('listar-autos/', listar_automoviles, name="listado_automoviles"),
    path('eliminar-autos/<id>/', eliminar_automovil, name="eliminar_automovil"),
    path('modificar-autos/<id>/', modificar_automovil, name="modificar_automovil")
]