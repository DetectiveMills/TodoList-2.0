from django.db import models

from django.contrib.auth import get_user_model
# from apps.users.models import User

# Create your models here.
User = get_user_model()

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_todo', verbose_name = 'Автор')
    title = models.CharField(max_length = 155, verbose_name = 'Заголовок задачи')
    description = models.TextField(verbose_name = 'Описание задачи')
    completed = models.BooleanField(default = False, verbose_name = 'Статус выполнения')
    created = models.DateTimeField(auto_now_add = True, verbose_name = 'Время')
    image = models.ImageField(upload_to='image/', verbose_name='Фото')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Todo list'
        verbose_name_plural = 'Todo list'

