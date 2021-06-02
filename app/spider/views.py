from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'spider.html', context)


def ai(request):
    # concat = request.POST
    # postBody = request.body
    # json_result = json.loads(postBody)
     
    # return HttpResponse(postBody['cjs'])
    return HttpResponse(request.GET['cjs'])
    # return HttpResponse(json_result)
   
    # return HttpResponse("ai ! ")


def spider(request):
    return HttpResponse("spider ! ")


def test(request):
    return HttpResponse("test ! ")


def tools(request):
    return HttpResponse("tools ! ")
