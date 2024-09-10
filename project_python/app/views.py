from django.shortcuts import render, redirect
from .forms import UsuarioCadastroForm, CustomLoginForm
from django.contrib.auth import authenticate, login

def tarefas(request):
    return render(request, 'tarefas.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def cadastro(request):
    if request.method == 'POST':
        form = UsuarioCadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UsuarioCadastroForm()
    
    return render(request, 'cadastro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST, request=request)  # Pass the request to the form
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('dashboard')
    else:
        form = CustomLoginForm()

    return render(request, 'login.html', {'form': form})