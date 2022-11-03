from rest_framework import serializers
from menu.models import Dish, Category


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