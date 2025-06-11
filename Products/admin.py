from django.contrib import admin
from .models import Categories, Products


@admin.register(Products)

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
