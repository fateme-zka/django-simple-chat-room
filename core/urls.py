from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

app_name = 'core'

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', login_custom, name='login'),
    path('logout/', logout_custom, name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),

]
