from rest_framework import generics

from orders.models import Orders, DishesInCart
from .serializers import DishSerializer, CategorySerializer, OrdersSerializer, DishesInCartSerializer
from menu.models import Dish, Category


class DishesList(generics.ListAPIView):
    serializer_class = DishSerializer

    def get_queryset(self):
        return Dish.objects.filter(is_published=True)


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()


class OrdersList(generics.ListCreateAPIView):
    serializer_class = OrdersSerializer

    def get_queryset(self):
        return Orders.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DICList(generics.ListAPIView):
    serializer_class = DishesInCartSerializer

    def get_queryset(self):
        return DishesInCart.objects.all()
