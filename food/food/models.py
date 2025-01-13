from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, related_name='products')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='food_img', blank=True, null=True)


    def get_absolute_url(self):
        return reverse('food_detail', args=[self.id])


    def __str__(self):
        return self.name