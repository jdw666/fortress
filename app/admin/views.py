from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {}
    context['test'] = 'test'
    return render(request, 'homepage.html', context)


def ai(request):
    return HttpResponse("ai ! ")


def spider(request):
    return HttpResponse("spider ! ")


def test(request):
    return HttpResponse("test ! ")


def tools(request):
    return HttpResponse("tools ! ")
