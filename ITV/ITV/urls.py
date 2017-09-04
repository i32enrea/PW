"""ITV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from inspeccion import views
from inspeccion.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='base.html'),name='base'),
    url(r'^login/', views.usuarioLogin, name='login'),
    url(r'^logout/', views.usuarioLogout, name='Logout'),
    url(r'^Coches/', views.mostrarCoches, name='coches'),
    url(r'^crearCoches/',views.crearCoches, name='Crear coches'),
    url(r'^editarCoches/(?P<coche_id>\d+)', views.editarCoches, name='Editar coches'),
    url(r'^detalleCoches/(?P<coche_id>\d+)', views.detalleCoches, name='Detalle Coches'),
    url(r'^Centros/', mostrarCentros.as_view(), name='centros'),
    url(r'^crearCentros/', crearCentros.as_view(), name='Crear centros'),
    url(r'^detalleCentros/(?P<centro_id>\d+)', detalleCentros.as_view(), name='Detalle Centros'),
    url(r'^editarCentros/(?P<pk>[\w-]+)$', editarCentros.as_view(), name='Editar Centros'),
    url(r'^eliminarCentros/(?P<pk>[\w-]+)$', eliminarCentros.as_view(), name='Borrar Centro'),
]
