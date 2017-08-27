from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from .models import Lista, Tareas
from django.views import generic
from .forms import ListaForm

def listaTareas(request, l_id):
    try:
        lista= Lista.objects.get(pk=l_id)
    except lista.DoesNotExist:
        raise Http404("La Lista No existe")
    return render(request, 'tareas/listado_tareas.html', {'lista': lista})


class IndexView(generic.ListView):
    template_name = 'tareas/index.html'
    context_object_name = 'listado'

    def get_queryset(self):
        """Return the last five published questions."""
        return Lista.objects.all()


class ListaCreateView(generic.CreateView):
    model = Lista
    # fields = ('question_text',)
    form_class = ListaForm
    success_url = reverse_lazy('tareas:index')
