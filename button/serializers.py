from rest_framework import serializers

from .models import Investment, Investor


class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = ("investor", "i_type", "interval", "amount", "percent")


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ("investor", "account", "total_invest", "profit")
