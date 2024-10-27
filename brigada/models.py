from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)  # Ej. 'Chef', 'Sous Chef', 'Cocinero'
    schedule = models.CharField(max_length=100)  # Ej. "Lunes a Viernes, 9am-5pm"

    def __str__(self):
        return f'{self.user.username} - {self.role}'
