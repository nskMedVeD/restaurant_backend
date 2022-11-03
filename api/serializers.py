from rest_framework import serializers
from menu.models import Dish


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

