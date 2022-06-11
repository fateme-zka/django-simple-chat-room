from django.shortcuts import render
from django.http import HttpResponse


def frontpage(request):

    context = {}
    return render(request, 'core/base.html', context)
