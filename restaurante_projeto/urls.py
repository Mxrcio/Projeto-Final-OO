from django.contrib import admin
from django.urls import path, include
from django.urls import path
from accounts import views as accounts_views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('welcome_app.urls')),
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('restaurante_projeto/', include('restaurante.urls')), 
    path('accounts/register/', accounts_views.register, name='register'),
    path('accounts/', include('accounts.urls')),  
    path('site_principal/', include('site_principal.urls')),
    path('site_principal/', include('pagamento_app.urls')),
]

