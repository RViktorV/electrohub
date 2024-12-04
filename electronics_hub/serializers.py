from rest_framework import serializers
from .models import Supplier, TradeNode


class SupplierSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Supplier.
    """

    class Meta:
        model = Supplier
        fields = [
            "id",  # Идентификатор поставщика
            "name",  # Название поставщика
            "email",  # Email
            "country",  # Страна
            "city",  # Город
            "street",  # Улица
            "house_number",  # Номер дома
        ]


class TradeNodeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели TradeNode.
    """
    supplier = SupplierSerializer(read_only=True)  # Отображение информации о поставщике
    supplier_id = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(),
        source="supplier",
        write_only=True,
        label="ID поставщика"
    )  # Поле для указания ID поставщика при создании/обновлении

    class Meta:
        model = TradeNode
        fields = [
            "id",  # Идентификатор узла
            "name",  # Название узла
            "email",  # Email
            "country",  # Страна
            "city",  # Город
            "street",  # Улица
            "house_number",  # Номер дома
            "product_name",  # Название продукта
            "product_model",  # Модель продукта
            "product_release_date",  # Дата выхода продукта
            "supplier",  # Информация о поставщике
            "supplier_id",  # Поле для указания ID поставщика
            "debt_to_supplier",  # Задолженность перед поставщиком
            "created_at",  # Дата создания
            "level",  # Уровень узла сети
        ]
        read_only_fields = ["debt_to_supplier", "created_at"]  # Поля только для чтения
