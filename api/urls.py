from django.urls import path
from . import views

urlpatterns = [
    path('dishes/', views.DishesList.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('orders/', views.OrdersList.as_view()),
    path('dic/', views.DICList.as_view()),

]
