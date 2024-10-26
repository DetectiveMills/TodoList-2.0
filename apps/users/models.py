from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(
        max_length=100,
        verbose_name='Email'
    )
    phone_number = models.CharField(
        max_length=100,
        verbose_name='Номер телефона'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано'
    )
    age = models.PositiveIntegerField(
        verbose_name='Возраст',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
