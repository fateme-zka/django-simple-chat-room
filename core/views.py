from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt

from .forms import SignUpForm


def frontpage(request):
    context = {}
    return render(request, 'core/base.html', context)


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
