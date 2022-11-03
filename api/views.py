from rest_framework import generics
from .serializers import DishSerializer
from menu.models import Dish


class DishesList(generics.ListAPIView):
    serializer_class = DishSerializer

    def get_queryset(self):
        return Dish.objects.filter(is_published=True)
