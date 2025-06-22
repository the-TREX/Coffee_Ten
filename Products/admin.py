from django.contrib import admin
from .models import Categories, Products, Comment



@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug' , 'created_at' , 'breed']
# admin.site.register(Products)
# admin.site.register(Categories)
admin.site.register(Comment)