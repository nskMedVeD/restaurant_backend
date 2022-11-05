from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from orders.models import Status, Orders, DishesInCart


class OrdersAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple}
    }


admin.site.register(DishesInCart)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Status)
