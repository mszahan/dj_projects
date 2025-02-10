from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('room/<slug:slug>', views.chatroom, name='chatroom')
]