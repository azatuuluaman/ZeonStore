from rest_framework import serializers

from .models import AboutUs, News, Helping


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class HelpingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Helping
        fields = '__all__'