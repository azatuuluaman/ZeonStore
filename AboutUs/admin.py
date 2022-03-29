from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from rest_framework.exceptions import ValidationError

from .models import AboutUs


class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = AboutUs
        fields = '__all__'

    def clean(self):
        if len(self.cleaned_data.get("title")) >= 8:
            raise ValidationError('Не больше 8 страниц')


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    form = ProductForm


class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
