from django.urls import path, include
from rest_framework.routers import DefaultRouter

from payouts.views import PayoutRequestViewSet

router = DefaultRouter()
router.register(r"api/payouts", PayoutRequestViewSet, basename="payout")

urlpatterns = [
    path("", include(router.urls)),
]
