from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def perfil_usuario(request):
    return render(request, 'users/perfil.html', {'usuario': request.user})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Usuario creado correctamente')
            return redirect('login')
    return render(request, 'users/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/menu/')  # O redirige a donde quieras
        else:
            messages.error(request, 'Credenciales inválidas')
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
