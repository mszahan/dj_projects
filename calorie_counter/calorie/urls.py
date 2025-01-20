from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='food_list'),
    path('delete/<int:id>', views.delete_consume, name='delete_consume'),
]