from django.conf import urls
from django.conf.urls import url,re_path
from django.urls import path,include,reverse
from fundacion import views

urlpatterns = [
    url(r'^$',views.HomePageView.as_view(),name="index"),
    url(r'pacientes/',views.HomePacientesViews.as_view(),name="pacientes"),
]