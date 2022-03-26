from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from .models import About_Us
# from .models import Image_About_Us


# class ImageInLine(admin.TabularInline):
#     model = Image_About_Us
#     max_num = 3
#     min_num = 1
class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = About_Us
        fields = '__all__'

@admin.register(About_Us)
class AboutUsAdmin(admin.ModelAdmin):
    form = ProductForm



class ProductAdmin(admin.ModelAdmin):
    form = ProductForm




