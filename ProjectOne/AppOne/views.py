from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def appone(request):
    template = loader.get_template('AppOne/myfirst.html')
    return HttpResponse(template.render())


def index(response):
    return HttpResponse("Hi, I am Sanket. <br> This is my first django project and app")
