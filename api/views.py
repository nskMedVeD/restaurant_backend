from rest_framework import generics
from .serializers import DishSerializer, CategorySerializer
from menu.models import Dish, Category


class DishesList(generics.ListAPIView):
    serializer_class = DishSerializer

    def get_queryset(self):
        return Dish.objects.filter(is_published=True)


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()
