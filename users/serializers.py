from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    transaction_type = serializers.CharField(
        source="get_transaction_type_display", read_only=True
    )

    class Meta:
        model = Transaction
        fields = ["id", "transaction_type", "amount", "created_at"]

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)


class TransactionCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(), source="user"
    )

    class Meta:
        model = Transaction
        fields = ["user_id", "transaction_type", "amount"]

    def validate(self, data):
        Transaction.validate_transaction(data["transaction_type"], data["amount"])
        return data

    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ("id", "username", "transactions")
        read_only_fields = ("id", "is_staff")

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
