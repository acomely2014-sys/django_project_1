from django.contrib import admin

from apps.products.models import ProductModel, CategoryModel


# Register your models here.
@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    search_fields = ['sort']
    readonly_fields = ('id', 'updated_at', 'created_at')
@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ['name']
    readonly_fields = ('id', 'updated_at', 'created_at')
