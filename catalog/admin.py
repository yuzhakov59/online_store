from django.contrib import admin
from catalog.models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'cat_description')
    list_filter = ('cat_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'picture','price', 'created_at', 'updated_at')
    list_filter = ('name','price',)
    search_fields = ('name', 'price',)