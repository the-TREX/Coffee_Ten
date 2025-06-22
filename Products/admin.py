from django.contrib import admin
from .models import Categories, Products, Comment


# @admin.register(Products)
# @admin.register(Comment)
# @admin.register(Categories)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name', 'slug']
#     prepopulated_fields = {'slug': ('name',)}

admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Comment)