from rest_framework import serializers

from .models import AboutUs, News, Helping, PublicOffer, Footer


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

class PublicOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicOffer
        fields = '__all__'

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = 'logo', 'description','num', 'link' , 'phone', 'gmail'