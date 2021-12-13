from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length= 200)

    def __str__(self):
        return self.name 

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()  

    class Meta:
        verbose_name_plural = 'Toppings'

    def __str__(self):
        return f"{self.name[:50]}..." #we dont want the whole text just the first 50 characters

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'comment'

    def __str__(self):
        return self.name