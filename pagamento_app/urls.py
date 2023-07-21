from django.urls import path
from . import views

urlpatterns = [
    path('pagamento/', views.pagamento_view, name='pagamento'),
    path('voltar_menu/', views.voltar_menu_view, name='voltar_menu'),
    path('retornar_menu/', views.retornar_menu, name='retornar_menu'),
    path('pagamento/feedback/', views.feedback_view, name='feedback'),  # URL para a página de feedback
]
