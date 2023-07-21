from django.shortcuts import render
from .models import Prato

def home(request):

    pratos = Prato.objects.all()

    return render(request, 'site_principal/home.html', {'pratos': pratos})

from django.shortcuts import render

def cart(request):
    cart_items = request.session.get('cart', [])
    total = 0
    for item in cart_items:
        total += item['price'] * item['quantity']
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})


from django.shortcuts import render

def pagamento_view(request):
    return render(request, 'pagamento.html')


from django.shortcuts import render, redirect
from .models import Prato
from .forms import PratoForm

def home(request):
    if request.method == 'POST':
        form = PratoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = PratoForm()

    pratos = Prato.objects.all()
    return render(request, 'site_principal/home.html', {'pratos': pratos, 'form': form})

def cart(request):
    cart_items = request.session.get('cart', [])
    total = 0
    for item in cart_items:
        total += item['price'] * item['quantity']
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

def pagamento_view(request):
    return render(request, 'pagamento.html')
