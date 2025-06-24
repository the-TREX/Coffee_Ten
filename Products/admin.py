from django.contrib import admin
from matplotlib.pyplot import title

from .models import Categories, Products, Comment


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


# class FilterByName(admin.SimpleListFilter):
#     title = "فیلتر بر اساس نام محصول"
#     parameter_name = "name"
#
#     def lookups(self, request, model_admin):
#         return (
#             ("daneghahve", "دانه قهوه"),
#             ("dastgah", "اسپرسوساز")
#         )
#
#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(name__icontains=self.value())


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'breed' , 'show_image']
    list_filter = ['breed', 'created_at']
    list_editable = ['breed',]
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


admin.site.register(Comment)
