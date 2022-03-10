from rest_framework import serializers

from .models import Investment, Investor


class InvestmentSerializer(serializers.ModelSerializer):
    """Serializing all the data of Investment model"""
    class Meta:
        model = Investment
        fields = '__all__'


class InvestorSerializer(serializers.ModelSerializer):
    """Serializing all the data of Investor model"""
    class Meta:
        model = Investor
        fields = '__all__'
