from django.conf.urls import url

from . import views

app_name = 'tareas'
urlpatterns = [
    url(r'^(?P<l_id>[0-9]+)/$', views.listaTareas, name='listado_tareas'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^crear_lista/$', views.ListaCreateView.as_view(), name='crear_lista'),
    url(r'^(?P<pk>[0-9]+)/modificar_lista$', views.ListaUpdateView.as_view(), name='modificar_lista'),
   
]
