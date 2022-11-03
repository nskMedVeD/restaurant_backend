from django.http import HttpResponse
from django.shortcuts import render

from menu.models import *

main_menu = ["Главная", "Корзина", "Поиск", "Логин"]


def index(request):
    dishes = Dish.objects.filter(is_published=True)
    categories = Category.objects.all()
    context = {
        'title': 'Главная страница',
        'main_menu': main_menu,
        'dishes': dishes,
        'categories': categories
    }

    return render(request, 'menu/index.html', context)


def contact(request):
    context = {
        'title': 'Контакты',
        'main_menu': main_menu
    }
    return render(request, 'menu/about.html', context)
