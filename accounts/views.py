from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserLoginForm
from .models import CustomUser
from django.http import JsonResponse

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Erro ao autenticar o usuário após o registro.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('site_principal')
            else:
                form.add_error(None, 'Credenciais inválidas. Verifique seu usuário e senha.')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        if CustomUser.objects.filter(username=username).exists() or CustomUser.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Nome de usuário ou email já cadastrados'}, status=400)

        new_user = CustomUser(username=username, email=email)
        new_user.save()

        return JsonResponse({'message': 'Cadastro realizado com sucesso!'})

    return render(request, 'accounts/register.html')
