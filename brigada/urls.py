from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenido a SousChef API")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('brigada.urls')),
    path('', home),  # Página de inicio básica
]
