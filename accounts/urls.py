from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('accounts/register/', views.register_user, name='register_user'),
    path('login/', views.user_login, name='user_login'),
]