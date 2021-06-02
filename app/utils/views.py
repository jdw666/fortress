from django.http import HttpResponse
from django.shortcuts import render
from app.testing.base.test.utils import base
import json
from django import http
# base.ceshi(protocal, tag, url, name)
import os

def index(request):
    context = {}
    context['test'] = 'test'
    return render(request, 'utils.html', context)


def ai(request):
    return HttpResponse("ai ! ")


def spider(request):
    return HttpResponse("spider ! ")


def test(request):
    return HttpResponse("test ! ")


def tools(request):
    return HttpResponse("tools ! ")


def api_search(request):
    return render(request, 'api_search.html')

def py_search(request):
    return render(request, 'py_search.html')

def php_search(request):
    return render(request, 'php_search.html')

def js_search(request):
    return render(request, 'js_search.html')

# 拉取功能
def s_pull(request):
    cmd = "git pull & git checkout dev "
    os.system(cmd)
    return http.JsonResponse({"code":200, "msg":"拉取成功"})

def filtrate(request):
    json_dict = json.loads(request.body.decode())
    dname = json_dict.get("dname")
    filtrate_s = json_dict.get("filtrate")
    if filtrate_s == "php_filtrate":
        dict_s = base.php_filtrate(dname)
    elif filtrate_s == "api_filtrate":
        dict_s = base.api_filtrate(dname)
    elif filtrate_s == "js_filtrate":
        dict_s = base.js_filtrate(dname)
    elif filtrate_s == "py_filtrate":
        dict_s = base.py_filtrate(dname)
    if dict_s:
        return http.JsonResponse({"code":200, "msg":dict_s})
    else:
        return http.JsonResponse({"code":201, "msg":dict_s})