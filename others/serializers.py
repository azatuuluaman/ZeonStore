from rest_framework import serializers

from .models import AboutUs, News, Helping, PublicOffer, Footer, FloatingButton, BackCall, MainPage, OurAdvantages, Header


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
        fields = '__all__'

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'

class FloatingButtonSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloatingButton
        fields = '__all__'


class BackCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackCall
        fields = '__all__'

class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPage
        fields = '__all__'

class OurAdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurAdvantages
        fields = '__all__'

