from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Room, Message


@login_required(login_url='core:login')
def rooms(request):
    rooms = Room.objects.all().order_by('-id')

    context = {'rooms': rooms}
    return render(request, 'room/rooms.html', context)


@login_required(login_url='core:login')
def room(request, the_slug):
    room = Room.objects.get(slug=the_slug)
    messages = Message.objects.filter(room=room)[:30]

    context = {
    'room': room,
    'messages': messages
    }
    return render(request, 'room/room.html', context)
