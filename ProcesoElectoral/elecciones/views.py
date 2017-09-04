from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.list import ListView
from models import Circunscripcion, Mesa, Resultado, Partido
import forms
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

class index_circunscripcion(ListView):
    context_object_name = 'circunscripciones'
    template_name = 'index_circunscripcion.html'
    def get_queryset(self):
        return Circunscripcion.objects.all()

class detalle_circunscripcion(DetailView):
    model = Circunscripcion
    template_name = 'detalle_circunscripcion.html'

class nueva_circunscripcion(CreateView):
    model = Circunscripcion
    template_name = 'nueva_circunscripcion.html'
    success_url = reverse_lazy('elecciones:index_circunscripcion')
    @method_decorator(login_required(login_url='users:login'))
    def dispatch(self, *args, **kwargs):
        return super(nueva_circunscripcion,self).dispatch(*args, **kwargs)
    def get(self, request, *args, **kwargs):
        if request.user.groups.filter(name='supervisor').count() == 0:
            raise PermissionDenied()
        return CreateView.get(self, request, *args, **kwargs)

class edita_circunscripcion(UpdateView):
    model = Circunscripcion
    template_name = 'edita_circunscripcion.html'
    success_url = reverse_lazy('elecciones:index_circunscripcion')
    @method_decorator(login_required(login_url='users:login'))
    def dispatch(self, *args, **kwargs):
        return super(edita_circunscripcion,self).dispatch(*args, **kwargs)
    def get(self, request, *args, **kwargs):
        if request.user.groups.filter(name='supervisor').count() == 0:
            raise PermissionDenied()
        return UpdateView.get(self, request, *args, **kwargs)

class elimina_circunscripcion(DeleteView):
    model = Circunscripcion
    template_name = 'elimina_circunscripcion.html'
    success_url = reverse_lazy('elecciones:index_circunscripcion')
    @method_decorator(login_required(login_url='users:login'))
    def dispatch(self, *args, **kwargs):
        return super(elimina_circunscripcion,self).dispatch(*args, **kwargs)
    def get(self, request, *args, **kwargs):
        if request.user.groups.filter(name='supervisor').count() == 0:
            raise PermissionDenied()
        return DeleteView.get(self, request, *args, **kwargs)

def index_mesa(request, pk):
    template_name = 'index_mesa.html'
    circunscripcion = get_object_or_404(Circunscripcion, pk=pk)
    mesas = Mesa.objects.filter(circunscripcion=circunscripcion)
    context = {'mesas':mesas, 'circunscripcion':circunscripcion}
    return render(request, template_name, context)

def detalle_mesa(request, pk):
    template_name = 'detalle_mesa.html'
    mesa = get_object_or_404(Mesa, pk=pk)
    context = {'mesa':mesa}
    return render(request, template_name, context)

@login_required(login_url='users:login')
def nueva_mesa(request, pk):
    template_name = 'nueva_mesa.html'
    if request.user.groups.filter(name='supervisor').count() == 0:
            raise PermissionDenied()
    circunscripcion = get_object_or_404(Circunscripcion, pk=pk)
    if request.method == 'POST':
        form = forms.NuevaMesa(request.POST)
        if form.is_valid():
            mesa = form.save(commit=False)
            mesa.circunscripcion = circunscripcion
            mesa.save()
            return redirect('elecciones:index_mesa', circunscripcion.pk)
    else:
        form = forms.NuevaMesa()
    context = {'form':form, 'circunscripcion':circunscripcion}
    return render(request, template_name, context)

@login_required(login_url='users:login')
def edita_mesa(request, pk):
    template_name = 'edita_mesa.html'
    if request.user.groups.filter(name='supervisor').count() == 0:
            raise PermissionDenied()
    object = get_object_or_404(Mesa, pk=pk)
    if request.method == 'POST':
        form = forms.NuevaMesa(request.POST, instance=object)
        if form.is_valid():
            mesa=form.save()
            return redirect('elecciones:index_mesa', mesa.circunscripcion.pk)
    else:
        form = forms.NuevaMesa(instance=object)
    context = {'form':form}
    return render(request, template_name, context)

@login_required(login_url='users:login')
def elimina_mesa(request, pk):
    if request.user.groups.filter(name='supervisor').count() == 0:
            raise PermissionDenied()
    object = get_object_or_404(Mesa, pk=pk)
    c = object.circunscripcion.pk
    if request.method == 'POST':
        object.delete()
        return redirect('elecciones:index_mesa', c)
    else:
        return render(request, 'elimina_mesa.html', {'mesa':object})

class index_resultado(ListView):
    context_object_name = 'resultados'
    template_name = 'index_resultado.html'
    def object(self):
        return get_object_or_404(Mesa, pk=self.kwargs['pk'])
    def get_queryset(self):
        return Resultado.objects.filter(mesa = self.object).order_by('votos')
    def get_context_data(self, **kwargs):
        context = super(index_resultado, self).get_context_data(**kwargs)
        context['mesa'] = self.object()
        return context

class nuevo_resultado(CreateView):
    model = Resultado
    template_name = 'nuevo_resultado.html'
    form_class = forms.AddResultado
    @method_decorator(login_required(login_url='users:login'))
    def dispatch(self, *args, **kwargs):
        return super(nuevo_resultado,self).dispatch(*args, **kwargs)
    def get(self, request, *args, **kwargs):
        if request.user.groups.filter(name='gestor').count() == 0:
            raise PermissionDenied()
        return CreateView.get(self, request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super(nuevo_resultado, self).get_context_data(**kwargs)
        context['mesa'] = get_object_or_404(Mesa, pk=self.kwargs['pk'])
        return context
    def form_valid(self, form):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            mesa = get_object_or_404(Mesa, pk=self.kwargs['pk'])
            resultado=form.save(commit=False)
            resultado.mesa = mesa
            resultado.save()
            return redirect('elecciones:index_resultado', self.kwargs['pk'])
        return CreateView.form_valid(self, form)

class asigna_escanyos(ListView):
	context_object_name = 'partidos'
	template_name = 'asigna_escanyos.html'
	def get(self, request, *args, **kwargs):
		for partido in Partido.objects.all():
		    partido.escanyos = 0
		    partido.votos = 0
		    partido.save()
		for circunscripcion in Circunscripcion.objects.all():
		    for partido in Partido.objects.all():
		        partido.votosCircunscripcion = 0
		        partido.save()
		    for mesa in Mesa.objects.filter(circunscripcion=circunscripcion):
		        for resultado in Resultado.objects.filter(mesa=mesa):
		            resultado.partido.votos += resultado.votos
		            resultado.partido.votosCircunscripcion += resultado.votos
		            resultado.partido.save()
		    masVotados = Partido.objects.order_by('-votosCircunscripcion')[:2]
		    ganador = Partido.objects.get(pk=masVotados[0].pk)
		    ganador.escanyos += circunscripcion.escanyos-1
		    ganador.save()
		    perdedor = masVotados[1]
		    perdedor.escanyos += 1
		    perdedor.save()
		    return ListView.get(self, request, *args, **kwargs)
	def get_queryset(self):
		return Partido.objects.order_by('-escanyos')
