from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    protien = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()

    def __str__(self):
        return self.name
    

class Consume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_consume')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='food_consume')

    def __str__(self):
        return f'{self.user.username} - {self.food.name}'