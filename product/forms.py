from django import forms
from .models import ProductGallery

class ImageForm(forms.ModelForm):

    class Meta:
        model = ProductGallery
        fields = [ProductGallery]

