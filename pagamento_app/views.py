from django.shortcuts import render, redirect

def pagamento_view(request):
    return render(request, 'pagamento.html')

def voltar_menu_view(request):
    return redirect(request, '/site_principal/')

from django.shortcuts import redirect

def retornar_menu(request):
    return redirect(request, 'site_principal')

def feedback_view(request):
    
    return render(request, 'feedback.html') 