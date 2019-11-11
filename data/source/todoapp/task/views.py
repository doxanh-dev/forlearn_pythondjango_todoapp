from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {'name': "HungDH"}
    return render(request, 'task/list.html', context)
