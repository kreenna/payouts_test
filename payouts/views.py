from rest_framework import viewsets

from .models import PayoutRequest
from .serializers import PayoutRequestSerializer
from .tasks import process_payout_request


class PayoutRequestViewSet(viewsets.ModelViewSet):
    """Вьюсет для заявок на оплату."""
    queryset = PayoutRequest.objects.all()
    serializer_class = PayoutRequestSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        process_payout_request.delay(instance.id)
