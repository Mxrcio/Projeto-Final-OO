from django.urls import path
from . import views

urlpatterns = [
    path('site_principal/pagamento/feedback/', views.feedback_page, name='feedback_page'),
]
