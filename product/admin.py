from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from .models import Product, ProductColor, ProductGallery, Collection
from ckeditor.widgets import CKEditorWidget


class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        if len(self.cleaned_data.get("color")) >= 8:
            raise ValidationError('Выберите не больше 8 цветов')
        if len(self.cleaned_data.get("cover_photo")) >= 8:
            raise ValidationError('Выберите не больше 8 изображений')



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm



@admin.register(ProductColor)
class Product_colorAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass
