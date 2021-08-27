from django import forms
from django.forms import widgets
from django.forms.widgets import DateInput
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import TemplateResponseMixin
from .models import PacienteFacade, Paciente 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms import ModelForm

class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request,"index.html",context=None)

class HomePacientesViews(LoginRequiredMixin,TemplateView):
    def get(self,request,**kwargs):
        pacienteFacade = PacienteFacade()
        return render(request,"pacientes.html",{"pacientes": pacienteFacade.buscarPacientes()})

class DetallePacienteView(LoginRequiredMixin,TemplateView):
    def get(self,request, **kwargs):
        id=int(kwargs["id"])
        pacienteFacade = PacienteFacade()
        return render(request, "paciente.html", {"paciente": pacienteFacade.buscarPaciente(id)})

class PacienteCreate(CreateView):
    model = Paciente
    template_name = './paciente_form.html'
    fields = '__all__'
    
class PacienteUpdate(UpdateView):
    model = Paciente
    template_name = './paciente_form.html'
    fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'fecha_nacimiento', 'sexo', 'peso', 'estatura','telefono']

class PacienteDelete(DeleteView):
    model = Paciente
    template_name = './paciente_confirm_delete.html'
    success_url = reverse_lazy('pacientes')