from django.urls import path

from .views import rooms, room

app_name = 'room'

urlpatterns = [
    path('', rooms, name='rooms'),
    path('room/<slug:the_slug>/', room, name='room'),

]
