from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def dhol(request):
    
    return HttpResponse("hello | world")


def dhola(request):
    
    return HttpResponse("hello | dunia")

def web_app(request):
    
    template = loader.get_template('index.html')
    return HttpResponse(template.render())