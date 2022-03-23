from django.contrib import admin
from .models import Product, Category, Product_item
from image.models import Image


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product_item)
class Product_itemAdmin(admin.ModelAdmin):
    pass

