from django.contrib import admin
from .models import Supplier, TradeNode


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Кастомизация админ-панели для модели Supplier (Поставщик)."""

    list_display = (
        "name",
        "email",
        "country",
        "city",
        "street",
        "house_number",
    )  # Поля для отображения в списке
    list_filter = ("country", "city")  # Фильтры по стране и городу
    search_fields = ("name", "email", "country", "city")  # Поля для поиска


@admin.register(TradeNode)
class TradeNodeAdmin(admin.ModelAdmin):
    """Кастомизация админ-панели для модели TradeNode (Узел сети)."""

    list_display = (
        "name",
        "level",
        "email",
        "country",
        "city",
        "street",
        "house_number",
        "product_name",
        "product_model",
        "supplier",
        "debt_to_supplier",
        "created_at",
    )  # Поля для отображения в списке
    list_filter = (
        "level",
        "country",
        "city",
        "supplier",
    )  # Фильтры по уровню, стране, городу и поставщику
    search_fields = (
        "name",
        "email",
        "country",
        "city",
        "product_name",
        "product_model",
    )  # Поля для поиска
    actions = ["clear_debt_to_supplier"]  # Кастомное действие

    def clear_debt_to_supplier(self, request, queryset):
        """Очистить задолженности перед поставщиком."""
        queryset.update(debt_to_supplier=0.00)
        self.message_user(request, "Задолженности перед поставщиками успешно очищены.")

    clear_debt_to_supplier.short_description = (
        "Очистить задолженности перед поставщиком"
    )
