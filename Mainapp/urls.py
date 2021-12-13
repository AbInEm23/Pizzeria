from django.urls import path 

from . import views 

app_name = 'Mainapp'
urlpatterns = [
    path('',views.index, name='index'),
    path('pizzas',views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/',views.pizza, name='pizza'),
    path('comment/<int:pizza_id>/',views.comment, name='comment'),
]

#for the third path in order for the view to know, it has to have an identifying number