from rest_framework import serializers

from .models import About_Us

class About_UsSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_Us
        fields = '__all__'