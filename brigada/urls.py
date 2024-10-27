from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, InventoryItemViewSet

# Configura el enrutador y registra los viewsets
router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'inventory', InventoryItemViewSet)

# Define las rutas del enrutador
urlpatterns = router.urls
