from django.shortcuts import render

from apps.todo.permissions import ToDoPermission
from .models import Task
from .serializers import TaskSerializer
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.
class TaskAPI(GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.RetrieveModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    # def get_permissions(self):
    #     if self.action in ('update', 'partial_update', 'destroy'):
    #         return (ToDoPermission(), )
    #     return (AllowAny(), )
    
    # def perform_create(self, serializer):
    #     return serializer.save(user=self.request.user)
