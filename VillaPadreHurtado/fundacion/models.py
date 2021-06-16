from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nombre=models.CharField(max_length=30)

class Paciente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    sex = [
        ('Femenino','Femenino'),
        ('Masculino','Masculino')
    ]
    sexo = models.CharField(max_length=9, choices=sex, default='Masculino')
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    estatura = models.IntegerField()
    telefono = models.IntegerField()
    pacientes = models.Manager()
    def __sts__(self):
        return self.nombre

class PacienteFacade:
    def __init__(self):
        self.PacienteFactory = Paciente.pacientes

    def buscarPacientes(self):
        return self.PacienteFactory.all()

    def buscarPaciente(self,id):
        return self.PacienteFactory.get(id=id)
