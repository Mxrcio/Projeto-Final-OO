from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('login/', views.login_page, name='login'),
    path('adicionar/prato/', views.adicionar_prato, name='adicionar_prato'),
    path('editar/prato/<int:id>/', views.editar_prato, name='editar_prato'),
]