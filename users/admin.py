from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User, Transaction

admin.site.register(User, UserAdmin)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "transaction_type", "amount", "formatted_created_at")
    list_filter = ("transaction_type", "created_at")
    search_fields = ("user__username", "transaction_type")
    ordering = ("-created_at",)

    def formatted_created_at(self, obj):
        return obj.created_at.strftime("%Y.%m.%d %H:%M:%S")

    formatted_created_at.short_description = "Created At"
