from django.contrib import admin

from .models import PayoutRequest


@admin.register(PayoutRequest)
class PayoutRequestAdmin(admin.ModelAdmin):
    """Отображение заявки на выплату в админке."""

    list_display = (
        "id",
        "status",
        "description",
        "amount",
        "currency",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "status",
        "currency",
    )
    search_fields = ("name",)
