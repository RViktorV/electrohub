from rest_framework import viewsets, permissions
from .models import Supplier, TradeNode
from .serializers import SupplierSerializer, TradeNodeSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    """
    Представление для управления поставщиками.
    """

    queryset = Supplier.objects.all()  # Запрос для выборки всех поставщиков
    serializer_class = SupplierSerializer  # Сериализатор для поставщиков
    permission_classes = [
        permissions.IsAuthenticated
    ]  # Только для авторизованных пользователей


class TradeNodeViewSet(viewsets.ModelViewSet):
    """
    Представление для управления узлами сети.
    """

    queryset = TradeNode.objects.all()  # Запрос для выборки всех узлов сети
    serializer_class = TradeNodeSerializer  # Сериализатор для узлов сети
    permission_classes = [
        permissions.IsAuthenticated
    ]  # Только для авторизованных пользователей

    def get_queryset(self):
        """
        Переопределение запроса для фильтрации данных.
        """
        queryset = super().get_queryset()
        # Фильтрация по стране (если параметр country передан в запросе)
        country = self.request.query_params.get("country")
        if country:
            queryset = queryset.filter(country__icontains=country)
        return queryset
