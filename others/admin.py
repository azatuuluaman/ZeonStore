from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from .models import AboutUs, News, Helping, Image, OurAdvantages, MainPage, PublicOffer, Footer, FloatingButton, BackCall, Header, ImageHelping


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

    def has_add_permission(self, request):
        has_add = super().has_add_permission(request)
        if has_add and Footer.objects.exists():
            has_add = False
        return has_add


admin.site.register(Header)

admin.site.register(FloatingButton)
admin.site.register(BackCall)


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        has_add = super().has_add_permission(request)
        if has_add and Footer.objects.exists():
            has_add = False
        return has_add



@admin.register(ImageHelping)
class ImageHelping(admin.ModelAdmin):
    def has_add_permission(self, request):
        has_add = super().has_add_permission(request)
        if has_add and Footer.objects.exists():
            has_add = False
        return has_add

