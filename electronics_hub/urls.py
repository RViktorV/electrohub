from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SupplierViewSet, TradeNodeViewSet

router = DefaultRouter()
router.register("suppliers", SupplierViewSet, basename="supplier")
router.register("tradenodes", TradeNodeViewSet, basename="tradenode")

urlpatterns = [
    path("api/", include(router.urls)),
]
