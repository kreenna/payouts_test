from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("payouts/", include("materials.urls", namespace="payouts")),
]
