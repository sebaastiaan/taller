from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nombre=models.CharField(max_length=30)

class Paciente:
    def __init__(self,id,nombre):
        self.id=id
        self.nombre=nombre

class PacienteFactory:
    def __init__(self):
        self.pacientes=[]
        self.pacientes.append(Paciente(1,"Sebastian"))
        self.pacientes.append(Paciente(2,"Pablo"))
    
    def obtener_pacientes(self):
        return self.pacientes
