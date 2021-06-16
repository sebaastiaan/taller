from django.conf.urls import url,re_path
from django.urls import path,include,reverse
from fundacion import views

urlpatterns = [
    url(r'^$',views.HomePageView.as_view(),name="index"),
    url(r'pacientes/',views.HomePacientesViews.as_view(),name="pacientes"),
    url(r'paciente/(?P<id>\d+)/$',views.DetallePacienteView.as_view(),name="paciente_read"),
    url(r'^paciente/create/$', views.PacienteCreate.as_view(success_url='/pacientes/'), name='paciente_create'),
    url(r'^paciente/(?P<pk>\d+)/update/$', views.PacienteUpdate.as_view(success_url='/pacientes/'), name='paciente_update'),
    url(r'^paciente/(?P<pk>\d+)/delete/$', views.PacienteDelete.as_view(success_url='/pacientes/'), name='paciente_delete'),
    path('accounts/', include('accounts.urls')),
    path("accounts/", include('django.contrib.auth.urls')),
]