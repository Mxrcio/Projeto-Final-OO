from django.shortcuts import render, redirect
from .models import Prato

def index(request):
    return render(request, 'index.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin' and password == '1234':
            return redirect('index')
        else:
            error_message = 'Credenciais inválidas. Tente novamente.'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def welcome_view(request):
    return render(request, 'welcome_app/welcome.html')

def listar_pratos(request):
    pratos = Prato.objects.all()
    return render(request, 'listar_pratos.html', {'pratos': pratos})

def adicionar_prato(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        tipo = request.POST['tipo']
        preco = request.POST['preco']
        prato = Prato(nome=nome, tipo=tipo, preco=preco)
        prato.save()
        return redirect('listar_pratos')
    return render(request, 'adicionar_prato.html')

def editar_prato(request, id):
    prato = Prato.objects.get(id=id)
    if request.method == 'POST':
        prato.nome = request.POST['nome']
        prato.tipo = request.POST['tipo']
        prato.preco = request.POST['preco']
        prato.save()
        return redirect('listar_pratos')
    return render(request, 'editar_prato.html', {'prato': prato})
