from django.contrib import admin

# Register your models here.
#pizza #toppings
from .models import Pizza, Topping


admin.site.register(Pizza)
admin.site.register(Topping)
