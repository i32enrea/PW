from django.shortcuts import render, redirect, get_object_or_404
from inspeccion.models import *
from  inspeccion.forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User, Group
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import ListView
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied
# Create your views here.

def usuarioLogin(request):
	if request.method=='POST':
	    formulario=AuthenticationForm(request.POST)
	    if formulario.is_valid:
	        usuario=request.POST['username']
	        clave=request.POST['password']
	        acceso=authenticate(username=usuario, password=clave)
	        if acceso is not None:
	            if acceso.is_active:
	                login(request,acceso)
	                return redirect('/')
	            else:
	                return redirect('/')
	        else:
	            return redirect('/')
	else:
	    formulario=AuthenticationForm()
	#contexto={'formulario':formulario}
	return render(request,'login.html',{'formulario':formulario})

@login_required(login_url='/login')
def usuarioLogout(request):
    logout(request)
    return redirect('/')

def mostrarCoches(request):
    coches=Coche.objects.all()
    return render(request,"ListarCoches.html",{'coches': coches})

def crearCoches(request):
    if request.method=='POST':
        coche=Coche()
        formulario=CochesForm(request.POST,instance=coche)
        if formulario.is_valid():
            formulario.save()
            return redirect('/Coches')
    else:
        formulario=CochesForm()

    #contexto={'formulario':formulario}

    return render(request,"crearCoche.html",{'formulario':formulario})

@login_required(login_url='/login')
@permission_required ('inspeccion.change_coche',raise_exception=True)
def editarCoches(request,coche_id):
    coche=get_object_or_404(Coche,pk=coche_id)
    if request.method=='POST':
        formulario=CochesForm(request.POST,instance=coche)
        if formulario.is_valid():
            formulario.save()
            return redirect('/Coches')
    else:
        formulario=CochesForm(instance=coche)
        contexto={'formulario':formulario}
        return render(request,"EditarCoches.html",contexto)

def detalleCoches(request,coche_id):
    cochespecifico=Coche.objects.get(pk=coche_id)
    contexto={'cochespecifico':cochespecifico}
    return render(request,"DetalleCoches.html",contexto)


class mostrarCentros(View):
    template_nombre="listarCentros.html"
    def get(self,request,*args,**kwargs):
        centros=Centros.objects.all()
        contexto={'centros':centros}
        return render(request,self.template_nombre,contexto)


class crearCentros(CreateView):
	model = Centros
	fields = ['nombre', 'direccion', 'telefono']
	template_name = 'CrearCentro.html'
	success_url = "/"
	@method_decorator(login_required(login_url='/login'))
	def dispatch(self, *args, **kwargs):
		return super(crearCentros,self).dispatch(*args, **kwargs)
	def get(self, request, *args, **kwargs):
		if request.user.groups.filter(name='Gestor').count() == 0:
			raise PermissionDenied()
		return CreateView.get(self, request, *args, **kwargs)

class detalleCentros(View):
    template_nombre="DetalleCentros.html"
    def get(self,request,*args,**kwargs):
        id=self.kwargs['centro_id']
        centroespecifico=get_object_or_404(Centros,pk=id)
        contexto={'centroespecifico':centroespecifico}
        return render(request,self.template_nombre,contexto)

class editarCentros(UpdateView):
	 model = Centros
	 fields = ['nombre','direccion', 'telefono']
	 template_name = 'EditarCentros.html'
	 success_url="/"
	 @method_decorator(login_required(login_url='/login'))
	 def dispatch(self, *args, **kwargs):
			return super(editarCentros,self).dispatch(*args, **kwargs)
	 def get(self, request, *args, **kwargs):
		if request.user.groups.filter(name='Gestor').count() == 0:
			raise PermissionDenied()
		return UpdateView.get(self, request, *args, **kwargs)

class eliminarCentros(DeleteView):
	model = Centros
	template_name = 'EliminarCentros.html'
	success_url="/Centros"
	@method_decorator(login_required(login_url='/login'))
	def dispatch(self, *args, **kwargs):
		return super(eliminarCentros,self).dispatch(*args, **kwargs)
	def get(self, request, *args, **kwargs):
		if request.user.groups.filter(name='Gestor').count() == 0:
			raise PermissionDenied()
		return DeleteView.get(self, request, *args, **kwargs)
