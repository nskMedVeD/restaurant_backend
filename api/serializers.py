from rest_framework import serializers
from menu.models import Dish, Category
from orders.models import Orders, DishesInCart


class DishSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dish
        fields = ['id',
                  'title',
                  'ingredients',
                  'image',
                  'wight',
                  'price',
                  'category',
                  ]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id',
                  'title',
                  ]


class DishesInCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = DishesInCart
        fields = ('product', 'count')


class OrdersSerializer(serializers.ModelSerializer):
    dishes = DishesInCartSerializer(many=True)

    class Meta:
        model = Orders
        fields = ('pk',
                  'user',
                  'status',
                  'dishes',
                  )
