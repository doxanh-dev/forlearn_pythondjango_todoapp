from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {'name': "HungDH"}
    return render(request, 'task/list.html', context)


def handler404(request, exception):
    context = {}
    return render(request, '404.html', context)
