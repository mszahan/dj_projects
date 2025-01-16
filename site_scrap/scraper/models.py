from django.db import models

# Create your models here.

class Link(models.Model):
    address = models.TextField(max_length=1000,blank=True, null=True)
    name = models.TextField(max_length=1000,blank=True, null=True)

    def __str__(self):
        return self.name



