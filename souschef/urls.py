from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Vista para la página de inicio
def home(request):
    return HttpResponse("Bienvenido a SousChef API")  # Respuesta simple para la raíz del sitio

# Lista de rutas principales de la aplicación
urlpatterns = [
    # Ruta para el panel de administración de Django
    path('admin/', admin.site.urls),
    
    # Ruta para obtener un nuevo par de tokens JWT (access y refresh)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Ruta para refrescar el token de acceso JWT usando el token de refresco
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Incluye las rutas de la aplicación 'brigada' bajo el prefijo 'api/'
    path('api/', include('brigada.urls')),  # Incluye las rutas de la app brigada
    
    # Página de inicio básica para la ruta '/'
    path('', home),  # Página de inicio
]
