from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=10)
    puesto = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    fechingreso = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'Empleado: {self.nombre} {self.apellidos}'