from django.contrib.auth.models import AbstractUser
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
