from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
                       url(r'circunscripciones$', views.index_circunscripcion.as_view(), name='index_circunscripcion'),
                       url(r'circunscripciones/nueva$', views.nueva_circunscripcion.as_view(), name='nueva_circunscripcion'),
                       url(r'circunscripciones/(?P<pk>\d+)$', views.detalle_circunscripcion.as_view(), name='detalle_circunscripcion'),
                       url(r'circunscripciones/(?P<pk>\d+)/edita$', views.edita_circunscripcion.as_view(), name='edita_circunscripcion'),
                       url(r'circunscripciones/(?P<pk>\d+)/elimina$', views.elimina_circunscripcion.as_view(), name='elimina_circunscripcion'),
                       url(r'circunscripciones/(?P<pk>\d+)/mesas$', views.index_mesa, name='index_mesa'),
                       url(r'circunscripciones/(?P<pk>\d+)/mesas/nueva$', views.nueva_mesa, name='nueva_mesa'),
                       url(r'mesas/(?P<pk>\d+)$', views.detalle_mesa, name='detalle_mesa'),
                       url(r'mesas/(?P<pk>\d+)/edita$', views.edita_mesa, name='edita_mesa'),
                       url(r'mesas/(?P<pk>\d+)/elimina', views.elimina_mesa, name='elimina_mesa'),
                       url(r'mesas/(?P<pk>\d+)/resultados$', views.index_resultado.as_view(), name='index_resultado'),
                       url(r'mesas/(?P<pk>\d+)/resultados/nuevo$', views.nuevo_resultado.as_view(), name='nuevo_resultado'),
                       url(r'asigna_escanyos$', views.asigna_escanyos.as_view(), name='asigna_escanyos'),
                       )