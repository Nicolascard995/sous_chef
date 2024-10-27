"""
URL configuration for souschef project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Importa el módulo admin de Django para habilitar la interfaz administrativa
from django.contrib import admin
# Importa las funciones path y include para gestionar rutas de la aplicación
from django.urls import path, include
# Importa las vistas de JWT para la autenticación de tokens
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  # Para obtener un nuevo token JWT
    TokenRefreshView,     # Para refrescar el token JWT existente
)

# Lista de rutas principales de la aplicación
urlpatterns = [
    # Ruta para el panel de administración de Django
    path('admin/', admin.site.urls),
    
    # Ruta para obtener un nuevo par de tokens JWT (access y refresh)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Ruta para refrescar el token de acceso JWT usando el token de refresco
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Incluye las rutas de la aplicación 'brigada' bajo el prefijo 'api/'
    # Esto permite gestionar las operaciones CRUD para la brigada de cocina
    path('api/', include('brigada.urls')),  # Incluye las rutas de la app brigada
]
