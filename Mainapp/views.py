from django.shortcuts import render
from .models import Pizza
# Create your views here.
# Two types of requests - post and get 

def index(request):
    return render(request, 'Mainapp/index.html')

#we use the same name as in the url file to match the function 
def pizzas(request):
    pizzas = Pizza.objects.order_by()

    context = {'pizzas':pizzas} 

    # the key is the variable used in the template/url
    #and the value is the variable used in the view.

    return render(request, 'Mainapp/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id= pizza_id)

    toppings = pizza.topping_set.all()
    context = {'pizza':pizza, 'toppings':toppings} 
    return render(request, 'Mainapp/pizza.html', context)