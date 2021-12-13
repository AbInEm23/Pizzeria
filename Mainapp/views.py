from django.shortcuts import redirect, render
from .models import Pizza
from .forms import PizzaForm
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

    #when the form is initially loaded into the screen is a get
    #post request posts to the db

def comment(request,pizza_id):
    pizza = Pizza.objects.get(id= pizza_id)
    if request.method != 'POST':
        form = PizzaForm()
    else:
        form = PizzaForm(data=request.POST)
        if form.is_valid(): #this will make sure your form complies w rules
            comment = form.save(commit= False)
            comment.pizza = pizza
            comment.save()
            return redirect('Mainapp:pizza', pizza_id = pizza_id)

    context = {'form':form, 'pizza':pizza}
    return render(request, 'Mainapp/comment.html',context)
