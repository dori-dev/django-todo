from django.contrib import admin
from .models import TodoItem


class TodoItemAdmin(admin.ModelAdmin):
    pass


admin.site.register(TodoItem, TodoItemAdmin)
