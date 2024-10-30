from django.db import models
from django.contrib.auth.models import User

class ChatHistory(models.Model):
    user_message = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.timestamp} - User: {self.user_message[:30]}..."


class Member(models.Model):
    ROLE_CHOICES = [
        ('Chef', 'Chef'),
        ('Sous Chef', 'Sous Chef'),
        ('Cocinero', 'Cocinero'),
        # Agrega más roles según lo necesites
    ]
    
    SCHEDULE_CHOICES = [
        ('Lunes a Viernes, 9am-5pm', 'Lunes a Viernes, 9am-5pm'),
        ('Lunes a Viernes, 2pm-10pm', 'Lunes a Viernes, 2pm-10pm'),
        ('Sábados y Domingos, 10am-6pm', 'Sábados y Domingos, 10am-6pm'),
        # Agrega más horarios según lo necesites
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)  # Opciones predefinidas para roles
    schedule = models.CharField(max_length=100, choices=SCHEDULE_CHOICES)  # Opciones predefinidas para horarios

    def __str__(self):
        return f'{self.user.username} - {self.role}'


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()  # Lista de ingredientes en formato JSON o texto
    steps = models.TextField()  # Descripción de pasos
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Costo total de la receta

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    UNIT_CHOICES = [
        ('kg', 'Kilogramo'),
        ('g', 'Gramo'),
        ('litro', 'Litro'),
        ('ml', 'Mililitro'),
        # Agrega más unidades según lo necesites
    ]

    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)  # Cantidad en stock
    unit = models.CharField(max_length=50, choices=UNIT_CHOICES)  # Unidades predefinidas
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.quantity} {self.unit})"
