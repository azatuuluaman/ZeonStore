from django.contrib import admin
from django import forms
from .models import Product, Product_item, Image , Product_number
from ckeditor.widgets import CKEditorWidget


class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm

@admin.register(Product_number)
class Product_numberAdmin(admin.ModelAdmin):
    pass

@admin.register(Product_item)
class Product_itemAdmin(admin.ModelAdmin):
    pass

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

