from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .apps import PayoutsConfig
from .views import PayoutRequestViewSet

app_name = PayoutsConfig.name

router = DefaultRouter()
router.register(r"api/payouts", PayoutRequestViewSet, basename="payout")

urlpatterns = [
    path("", include(router.urls)),
]
