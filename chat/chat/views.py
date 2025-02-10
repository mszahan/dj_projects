from django.shortcuts import render, get_object_or_404
from .models import ChatRoom


def index(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'index.html', {'chatrooms': chatrooms})

def chatroom(request, slug):
    chatroom = get_object_or_404(ChatRoom, slug=slug)
    return render(request, 'room.html', {'chatroom':chatroom})
