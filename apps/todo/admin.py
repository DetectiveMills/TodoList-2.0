from django.contrib import admin
from .models import Task

# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'completed']
    search_fields = ['id', 'title', 'completed']
    list_filter = ['id', 'title', 'completed']
