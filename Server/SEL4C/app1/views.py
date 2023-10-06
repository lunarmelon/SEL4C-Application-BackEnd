from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets, permissions
from django.views.decorators.csrf import csrf_exempt
from SEL4C.app1.serializers import UserSerializer, GroupSerializer
from .models import Usuario, Administrador
from .serializers import *
import requests
from django.contrib import messages
from django.urls import reverse
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
import hashlib as h

def home(request):
    return render(request, "app1/homepage.html")

def register(request):
    return render(request, "app1/register.html")

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('correo','').strip()
        password = request.POST.get('password','').strip()
        print(password)
        h_password = h.sha256(password.encode()).hexdigest()
        print(h_password)

        user = authenticate(request, email=email, password=h_password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Correo o contraseña inválidos')

    return render(request, "app1/login.html")

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('http://localhost:8000/SEL4C/')

@login_required(login_url='login')
def dashboard(request):
    return render(request, "app1/index.html")

@login_required(login_url='login')
def usersList(request):
    users = list(Usuario.objects.all())
    ctx = {'users': users}
    return render(request, "app1/users-list.html", ctx)

@login_required(login_url='login')
def userDetails(request, pk):
    usuario = Usuario.objects.get(id = pk)
    ctx = {'usuario':usuario}
    return render(request, "app1/user-details.html", ctx)

@login_required(login_url='login')
def buttons(request):
    return render(request, "app1/ui-buttons.html")

@login_required(login_url='login')
def cards(request):
    return render(request, "app1/ui-card.html")


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset  = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AdministradorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that MyModel to be viewed or edited.
    """
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that MyModel to be viewed or edited.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ProgresoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that MyModel to be viewed or edited.
    """
    queryset = Progreso.objects.all()
    serializer_class = ProgresoSerializer

class ActividadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that MyModel to be viewed or edited.
    """
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class EntregaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that MyModel to be viewed or edited.
    """
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer

class PreguntaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that MyModel to be viewed or edited.
    """
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer


class AutodiagnosticoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that MyModel to be viewed or edited.
    """
    queryset = Autodiagnostico.objects.all()
    serializer_class = AutodiagnosticoSerializer

class RespuestaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that MyModel to be viewed or edited.
    """
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer
