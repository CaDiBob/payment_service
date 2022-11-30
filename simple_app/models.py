from django.core.validators import MinValueValidator
from django.db import models


class Currency(models.TextChoices):
    USD = 'usd', 'USD'
    RUB = 'rub', 'RUB'


class Item(models.Model):
    name = models.CharField(
        'Наименование',
        max_length=255
    )
    descriptions = models.TextField(
        'Описание',
    )
    price = models.DecimalField(
        'Цена',
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    currency = models.CharField(
        max_length=15,
        choices=Currency.choices,
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} цена {self.price}'

