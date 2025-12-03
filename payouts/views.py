from rest_framework import viewsets

from .models import PayoutRequest
from .serializers import PayoutRequestSerializer
from .tasks import process_payout_request


class PayoutRequestViewSet(viewsets.ModelViewSet):
    """Управление заявками на выплату средств."""

    queryset = PayoutRequest.objects.all()
    serializer_class = PayoutRequestSerializer

    def perform_create(self, serializer) -> None:
        """Создание с вызовом celery."""
        instance = serializer.save()
        process_payout_request.delay(instance.id)
