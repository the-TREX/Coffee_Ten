from django.contrib import admin
from .models import Categories, Products

admin.site.register(Products)


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
