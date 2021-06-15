from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import TemplateResponseMixin
from .models import PacienteFactory

class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request,"index.html",context=None)

class HomePacientesViews(TemplateView):
    def get(self,request,**kwargs):
        pacienteFactory=PacienteFactory()
        return render(request,"pacientes.html",{"pacientes": pacienteFactory.pacientes})