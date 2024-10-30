from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    RecipeViewSet,
    InventoryItemViewSet,
    whatsapp_bot,
    inventory_cost_report,
    chat_summary_report
)

# Configura el enrutador y registra los viewsets
router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'inventory', InventoryItemViewSet)

# Define las rutas del enrutador y añade las rutas adicionales
urlpatterns = router.urls + [
    path('whatsapp/', whatsapp_bot, name='whatsapp-bot'),
    path('reports/inventory-cost/', inventory_cost_report, name='inventory-cost-report'),
    path('reports/chat-summary/', chat_summary_report, name='chat-summary-report'),
]
