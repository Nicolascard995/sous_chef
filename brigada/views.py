import os
import openai
from dotenv import load_dotenv
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Sum, Count
from twilio.twiml.messaging_response import MessagingResponse
from .models import Member, Recipe, InventoryItem, ChatHistory
from .serializers import MemberSerializer, RecipeSerializer, InventoryItemSerializer

# Cargar variables de entorno y configurar la API de OpenAI
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

@api_view(['POST'])
def whatsapp_bot(request):
    """Bot de WhatsApp que responde a comandos básicos: 'recipe' o 'inventory'."""
    incoming_msg = request.data.get('Body', '').strip().lower()
    response = MessagingResponse()
    msg = response.message()

    if 'recipe' in incoming_msg:
        recipes = Recipe.objects.all()
        recipes_text = "\n".join([f"{recipe.name}: ${recipe.cost}" for recipe in recipes])
        msg.body("Available Recipes:\n" + recipes_text)
    elif 'inventory' in incoming_msg:
        inventory = InventoryItem.objects.all()
        inventory_text = "\n".join([f"{item.name}: {item.quantity} {item.unit}" for item in inventory])
        msg.body("Current Inventory:\n" + inventory_text)
    else:
        msg.body("Sorry, I didn't understand that. Send 'recipe' or 'inventory'.")

    return Response(str(response), content_type="application/xml")

@api_view(['GET'])
def inventory_cost_report(request):
    """Reporte de costos totales en el inventario."""
    total_cost = InventoryItem.objects.aggregate(total=Sum('quantity'))['total']
    return Response({"total_inventory_cost": total_cost})

@api_view(['GET'])
def chat_summary_report(request):
    """Reporte resumido de mensajes en el historial de chat."""
    total_messages = ChatHistory.objects.count()
    common_questions = ChatHistory.objects.values('user_message').annotate(count=Count('user_message')).order_by('-count')[:5]

    report = {
        "total_messages": total_messages,
        "common_questions": [{"message": q['user_message'], "count": q['count']} for q in common_questions]
    }
    return Response(report)

# Vistas para la API RESTful con autenticación y permisos
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
