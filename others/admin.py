from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from rest_framework.exceptions import ValidationError

from .models import AboutUs, News, Helping, Image


class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = AboutUs
        fields = '__all__'



@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    form = ProductForm


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm

@admin.register(News)
class News(admin.ModelAdmin):
    form = ProductForm

admin.site.register(Helping)

admin.site.register(Image)
