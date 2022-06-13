from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import auth_logout
from .forms import SignUpForm


def frontpage(request):
    context = {}
    return render(request, 'core/frontpage.html', context)


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('core:frontpage')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})


def login_custom(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('core:frontpage')

    return render(request, 'core/login.html')


def logout_custom(request, ):
    auth_logout(request)
    return redirect('core:frontpage')
