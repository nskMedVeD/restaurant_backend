from django.urls import path
from . import views

urlpatterns = [
    path('dishes/', views.DishesList.as_view()),
    path('categories/', views.CategoryList.as_view()),
]
