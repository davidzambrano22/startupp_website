from django.contrib import admin
from .models import Caterogy, Product, Subcategory

# Register your models here.
@admin.register(Caterogy)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'subcategory']
    list_filter = ['subcategory']
    list_editable = ['price']
    prepopulated_fields = {'slug': ('name',)}