from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Transaction


@receiver(post_save, sender=Transaction)
def send_transaction_email(sender, instance, created, **kwargs):
    if created:
        print(f"New transaction created: {instance}")

        def send_mail(subject, message, from_email, recipient_list, ):
            pass

        print(
            f"Email sent: New transaction {instance.id} for user {instance.user.username}, amount: {instance.amount}, type: {instance.transaction_type}."
        )
