from django.http import HttpResponse
from app.ai.apps import AiConfig
from django.shortcuts import render


def index(request):
    context = {}
    context['test'] = 'test'
    return render(request, 'ai.html', context)


def init(request):
    model_save_path = 'app/ai/model.h5'
    model = AiConfig(model_save_path)
    result = model.predictNum(19)
    return HttpResponse(result)


def spider(request):
    return HttpResponse("spider ! ")


def test(request):
    return HttpResponse("test ! ")


def tools(request):
    return HttpResponse("tools ! ")
