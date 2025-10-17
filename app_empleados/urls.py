from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('<int:id>', views.ver_empleado, name='ver_empleados'),
    path('agregar/', views.agregar_empleado, name='agregar_empleados'),
    path('editar/<int:id>/', views.editar_empleado, name='editar_empleados'),
    path('borrar/<int:id>/', views.borrar_empleado, name='borrar_empleados'),
    ]