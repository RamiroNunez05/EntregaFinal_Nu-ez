from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Familiar, Compra, Vuelo
from .forms import CompraForm, VueloForm, FamiliarForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render( request, "proyecto3_app/home.html")

@login_required
def crear_familiar(request):
    if request.method == 'POST':
        form = FamiliarForm(request.POST)
        if form.is_valid():
            familiar = Familiar(
                nombre=form.cleaned_data['nombre'],
                edad=form.cleaned_data['edad'],
                parentesco=form.cleaned_data['parentesco'],
                fecha_nacimiento=form.cleaned_data['fecha_nacimiento'],
            )
            familiar.save()
            return redirect('listar-familiares')

    form = FamiliarForm()
    return render(request, 'proyecto3_app/crear-familiar.html', {"form": form})

@login_required
def listar_familiares(request):
    familiares = Familiar.objects.all()
    return render(request, 'proyecto3_app/listar-familiares.html', {"familiares": familiares})

@login_required
def buscar_compras(request):
    if request.method == 'GET':
        descripcion = request.GET.get('descripcion', '')
        compras = Compra.objects.filter(descripcion__icontains=descripcion)
        return render(request, 'proyecto3_app/ultimas-compras.html', {"compras": compras, "descripcion": descripcion})

@login_required
def reservar_vuelo(request):
    if request.method == 'POST':
        form = VueloForm(request.POST)
        if form.is_valid():
            vuelo = Vuelo(
            origen = form.cleaned_data['origen'],
            destino = form.cleaned_data['destino'],
            fecha_salida = form.cleaned_data['fecha_salida'],
            horario = form.cleaned_data['horario'],
            precio = form.cleaned_data['precio'],
        )
        vuelo.save()
        return redirect('vuelos-reservados')

    form = VueloForm()
    return render(request, 'proyecto3_app/reservar-vuelo.html', {"form": form})

@login_required
def vuelos_reservados(request):
    vuelos = Vuelo.objects.all().order_by('-id')
    return render(request, 'proyecto3_app/vuelos-reservados.html', {"vuelos": vuelos})

@login_required
def buscar_vuelos(request):
    if request.method == 'GET':
        destino = request.GET.get('destino', '')
        vuelos = Vuelo.objects.filter(destino__icontains=destino)
        return render(request, 'proyecto3_app/vuelos-reservados.html', {"vuelos": vuelos, "destino": destino})

class CompraCreateView(LoginRequiredMixin, CreateView):
    model = Compra
    form_class = CompraForm
    template_name = 'proyecto3_app/tienda-compra.html'
    success_url = reverse_lazy('ultimas-compras')


class CompraListView(LoginRequiredMixin, ListView):
    model = Compra
    template_name = 'proyecto3_app/ultimas-compras.html'
    context_object_name = 'compra'


class CompraUpdateView(LoginRequiredMixin, UpdateView):
    model = Compra
    form_class = CompraForm
    template_name = 'proyecto3_app/tienda-compra.html'
    success_url = reverse_lazy('ultimas-compras')


class CompraDetailView(LoginRequiredMixin, DetailView):
    model = Compra
    template_name = 'proyecto3_app/detalle-compra.html'
    context_object_name = 'compra'


class CompraDeleteView(LoginRequiredMixin, DeleteView):
    model = Compra
    template_name = 'proyecto3_app/eliminar-compra.html'
    success_url = reverse_lazy('ultimas-compras')

def about(request):
    return render(request, 'proyecto3_app/about.html')