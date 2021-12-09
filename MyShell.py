import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from Mainapp.models import Pizza,Topping
#NO-SQL
pizzas = Pizza.objects.all()

for pizza in pizzas:
    print(pizza.id)
    print(pizza.name)
    print()

p = Pizza.objects.get(id= 1)
print(p)

toppings = p.topping_set.all()

for t in toppings:
    print(t)