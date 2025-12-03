from django.db import models


class PayoutRequest(models.Model):
    """Модель заявки на выплату с полями суммы выплаты, вылюты, реквизитов, статуса и описания."""

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    recipient_info = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
