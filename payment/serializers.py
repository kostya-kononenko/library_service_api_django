from rest_framework import serializers

from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            "id",
            "user",
            "status",
            "payment_type",
            "borrowing",
            "session_url",
            "session_id",
            "money_to_pay",
        )


class PaymentListSerializer(PaymentSerializer):
    user = serializers.CharField(
        source="user.email",
        read_only=True)
    borrowing = serializers.CharField(
        source="borrowing.book.title",
        read_only=True)

    class Meta:
        model = Payment
        fields = (
            "id",
            "user",
            "status",
            "payment_type",
            "borrowing",
            "session_url",
            "session_id",
            "money_to_pay",
        )


class PaymentDetailSerializer(PaymentSerializer):
    user = serializers.CharField(
        source="user.email")
    borrowing_book = serializers.CharField(
        source="borrowing.book.title")
    expected_return = serializers.CharField(
        source="borrowing.expected_return")

    class Meta:
        model = Payment
        fields = (
            "id",
            "user",
            "status",
            "payment_type",
            "borrowing_book",
            "expected_return",
            "session_url",
            "session_id",
            "money_to_pay",
        )
