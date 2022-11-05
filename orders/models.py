from django.db import models
from django.contrib.auth.models import User

import menu.models


class Status(models.Model):
    title = models.CharField(max_length=30, verbose_name='Статус заказа')

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'

    def __str__(self):
        return f'Статус {self.title}'


class DishesInCart(models.Model):
    product = models.ForeignKey(menu.models.Dish,
                                on_delete=models.CASCADE,
                                verbose_name='Продукт'
                                )
    count = models.IntegerField(default=0,
                                verbose_name='Количество'
                                )

    class Meta:
        verbose_name = 'Продукт в корзине'
        verbose_name_plural = 'Продукты в корзине'

    def __str__(self):
        return f'{self.product} - {self.count} штук'


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    created = models. DateTimeField(auto_now_add=True, verbose_name='Время заказа')
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        verbose_name='Статус заказа',
        default=1
    )
    dishes = models.ManyToManyField(DishesInCart,
                                    verbose_name='Блюда в заказе'
                                    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ {self.pk} от пользователя {self.user} от {self.created}'

