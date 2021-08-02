from django.contrib import admin
from .models import Category, Task


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    list_filter = ('created', 'updated')
    search_fields = ('name',)
    ordering = ('created',)


@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'created', 'updated', 'expire_date')
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ('created', 'updated', 'expire_date', 'is_done')
    search_fields = ('name', 'slug')
    ordering = ('created',)
    raw_id_fields = ('category',)

