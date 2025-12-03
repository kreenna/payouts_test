from unittest.mock import patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from payouts.models import PayoutRequest


class PayoutRequestViewSetTests(APITestCase):
    """Тесты для всех запросов по заявке на выплату."""

    def setUp(self):
        """Информация для тестов."""
        self.payout = PayoutRequest.objects.create(
            amount=50.00,
            currency="USD",
            recipient_info="recipient@example.com",
            status="pending",
            description="Initial payout"
        )
        self.list_url = reverse("payouts:payout-list")
        self.detail_url = reverse("payouts:payout-detail", args=[self.payout.id])

    def test_list_payouts(self):
        """Тест вывода списка всех заявок."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # проверяем количество элементов
        self.assertEqual(response.data[0]["id"], self.payout.id)

    def test_retrieve_payout(self):
        """Тест вывода получения конкретной заявки."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.payout.id)

    @patch("payouts.tasks.process_payout_request.delay")
    def test_create_payout_and_trigger_celery_task(self, mock_celery_task):
        """Тест создания заявки и проверка вызова celery."""
        data = {
            "amount": "123.45",
            "currency": "EUR",
            "recipient_info": "newrecipient@example.com",
            "description": "Test payout create"
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(PayoutRequest.objects.filter(id=response.data["id"]).exists())
        mock_celery_task.assert_called_once()

    def test_partial_update_status(self):
        """Тест обновления информации о заявке."""
        patch_data = {"status": "processing"}
        response = self.client.patch(self.detail_url, patch_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.payout.refresh_from_db()
        self.assertEqual(self.payout.status, "processing")

    def test_delete_payout(self):
        """Тест удаления заявки."""
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(PayoutRequest.objects.filter(id=self.payout.id).exists())

    def test_create_invalid_amount(self):
        """Тест создания с некорректной суммой."""
        data = {
            "amount": "-1.0",
            "currency": "USD",
            "recipient_info": "abc"
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("amount", response.data)

    def test_create_invalid_currency(self):
        """Тест создания с некорректной валютой."""
        data = {
            "amount": "10.0",
            "currency": "US",
            "recipient_info": "abc"
        }
        response = self.client.post(self.list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("currency", response.data)
