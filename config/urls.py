from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("payouts/", include("payouts.urls", namespace="payouts")),
]
