from django.contrib import admin
from meal.models import ToDo, Category, NeedItem


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'name', 'category', 'description', 'start_date',
        'end_date', 'is_completed'
    ]
    search_fields = ['user', 'name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']


@admin.register(NeedItem)
class NeedItemAdmin(admin.ModelAdmin):
    list_display = ['todo' ,'name', 'date']
    search_fields = ['name']
