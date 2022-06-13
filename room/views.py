from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Room


@login_required(login_url='core:login')
def rooms(request):
    rooms = Room.objects.all().order_by('-id')

    context = {'rooms': rooms}
    return render(request, 'room/rooms.html', context)


@login_required(login_url='core:login')
def room(request, the_slug):
    room = Room.objects.get(slug=the_slug)

    context = {'room': room}
    return render(request, 'room/room.html', context)
