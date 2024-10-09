from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class User(AbstractUser):
    pass


class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ("debit", "Debit"),
        ("credit", "Credit"),
        ("transfer", "Transfer"),
        ("refund", "Refund"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="transactions"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction({self.user.username}, {self.amount}, {self.transaction_type}, {self.created_at})"

    @staticmethod
    def validate_transaction(transaction_type, amount):
        """
        Validates that the transaction is correct:

        - If the transaction amount is negative, the type must be 'refund'.
        - If the transaction type is 'refund', the amount must be negative.
        """
        if amount < 0 and transaction_type != "refund":
            raise ValidationError(
                "Negative transactions can only be of the 'refund' type."
            )
        if transaction_type == "refund" and amount >= 0:
            raise ValidationError("The 'refund' amount must be negative.")

    def clean(self):
        Transaction.validate_transaction(self.transaction_type, self.amount)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
