from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Room

@login_required
def rooms(reqeuest):
    rooms = Room.objects.all()

    return render(reqeuest, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    
    return render(request, 'room/room.html', {'room': room})
