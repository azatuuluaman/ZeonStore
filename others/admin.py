from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from .models import AboutUs, News, Helping, Image, OurAdvantages, MainPage, PublicOffer, Footer, FloatingButton, NumberForFooter, BackCall


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
admin.site.register(OurAdvantages)
admin.site.register(MainPage)

@admin.register(PublicOffer)
class PublicOffer(admin.ModelAdmin):
    form = ProductForm


admin.site.register(Footer)
admin.site.register(FloatingButton)
admin.site.register(NumberForFooter)
admin.site.register(BackCall)
