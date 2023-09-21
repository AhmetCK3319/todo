from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=[
        'task',
        'is_complate',
        'created_at',
        'updated_at',
    ]
    search_fields=[
        'task',
    ]

# Register your models here.
