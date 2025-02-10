from django.shortcuts import render
from .models import ChatRoom


def index(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'index.html', {'chatrooms': chatrooms})
