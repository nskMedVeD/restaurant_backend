from django.urls import path
from . import views

urlpatterns = [
    path('dishes/', views.DishesList.as_view()),

]