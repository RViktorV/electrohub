from django.db import models

NULLABLE = {"blank": True, "null": True}

class Supplier(models.Model):
    """
    Модель для представления поставщика оборудования.
    """
    name = models.CharField(max_length=255)  # Название поставщика
    email = models.EmailField()                # Email поставщика
    country = models.CharField(max_length=100) # Страна поставщика
    city = models.CharField(max_length=100)    # Город поставщика
    street = models.CharField(max_length=255)  # Улица поставщика
    house_number = models.CharField(max_length=10)  # Номер дома

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"
    def __str__(self):
        """Возвращает строковое представление поставщика."""
        return self.name

class TradeNode(models.Model):
    """
    Модель для представления узла сети (завод, розничная сеть, индивидуальный предприниматель).
    """
    LEVEL_CHOICES = [
        (0, 'Завод'),                  # Уровень 0 - Завод
        (1, 'Розничная сеть'),         # Уровень 1 - Розничная сеть
        (2, 'Индивидуальный предприниматель'),  # Уровень 2 - ИП
    ]

    name = models.CharField(max_length=255, verbose_name="Название")  # Название узла сети
    email = models.EmailField(verbose_name="Email") # Email узла сети
    country = models.CharField(max_length=100, verbose_name="Страна") # Страна узла сети
    city = models.CharField(max_length=100, verbose_name="Город")    # Город узла сети
    street = models.CharField(max_length=100, verbose_name="Улица")  # Улица узла сети
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")  # Номер дома узла сети
    product_name = models.CharField(max_length=255)  # Название продукта
    product_model = models.CharField(max_length=255)  # Модель продукта
    product_release_date = models.DateField()  # Дата выхода продукта на рынок
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Поставщик", related_name="clients", **NULLABLE)  # Поставщик узла сети
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Задолженность", default=0.00)  # Задолженность перед поставщиком
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")  # Время создания узла сети
    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name="Уровень")  # Уровень узла сети

    class Meta:
        verbose_name = "Узел сети"
        verbose_name_plural = "Узлы сети"

    def __str__(self):
        """Возвращает строковое представление узла сети."""
        return self.name
