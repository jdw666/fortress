from django.http import HttpResponse
from django.shortcuts import render
from .base.test.utils import base
import os


def index(request):
    context = {}
    context['test'] = 'test'
    return render(request, 'testing.html', context)

    
def test_build(request):
    # context = base.cmd('bash','build_jobs.sh')
    return render(request, 'test_build.html')

def pro_build(request):
    # context = base.cmd('bash','build_jobs.sh')
    return render(request, 'pro_build.html')

def create(request):
    base.cmd('python','test_create_case.py')
    return render(request, 'create.html')


def runner(request):
    base.cmd('python','test_case_auto.py')
    return render(request, 'runner.html')

def report(request):
    context = base.sqlReport("'error'")
    return render(request, 'report.html', {'report': context})
