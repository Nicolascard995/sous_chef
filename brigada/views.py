from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view  # Importa api_view
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db.models import Sum
from .models import Member, Recipe, InventoryItem
from .serializers import MemberSerializer, RecipeSerializer, InventoryItemSerializer


@api_view(['GET'])
def inventory_cost_report(request):
    total_cost = InventoryItem.objects.aggregate(total=Sum('quantity'))['total']
    return Response({"total_inventory_cost": total_cost})


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
