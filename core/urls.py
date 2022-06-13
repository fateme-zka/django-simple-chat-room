from django.urls import path

from .views import *


app_name = 'core'

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),

]
