import time

from celery_app import shared_task
from .models import PayoutRequest


@shared_task
def process_payout_request(payout_id):
    """Процесс обработки заявки."""
    try:
        payout = PayoutRequest.objects.get(id=payout_id)
        payout.status = "processing"
        payout.save()
        time.sleep(10)  # имитация обработки
        payout.status = "completed"
        payout.save()
    except PayoutRequest.DoesNotExist:
        # логика при отсутствии заявки
        pass
