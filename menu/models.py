from django.db import models


class Category(models.Model):

    title = models.CharField(max_length=100, verbose_name='Категория')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Dish(models.Model):

    title = models.CharField(max_length=100, verbose_name='Название блюда')
    ingredients = models.CharField(max_length=255, verbose_name='Состав блюда')
    image = models.ImageField(upload_to='images/dishes/', blank=True, verbose_name='Изображение блюда')
    wight = models.IntegerField(default=0, blank=True, verbose_name='Масса порции')
    price = models.IntegerField(default=0, blank=True,  verbose_name='Цена порции')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория блюда', blank=True)
    is_published = models.BooleanField(default=False, verbose_name='Отображение на сайте')

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.title
