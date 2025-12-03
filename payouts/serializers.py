from rest_framework import serializers

from .models import PayoutRequest


class PayoutRequestSerializer(serializers.ModelSerializer):
    """Сериализатор для модели заявки на выплату."""

    class Meta:
        model = PayoutRequest
        fields = "__all__"

    @staticmethod
    def validate_amount(value):
        if value <= 0:
            raise serializers.ValidationError("Сумма должна быть больше 0.")
        return value

    @staticmethod
    def validate_currency(value):
        if len(value) != 3:
            raise serializers.ValidationError("Валюта должна быть представлена кодом из трёх символов (RUB и др.)")
        return value.upper()
