from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return  HttpResponse("Hello")


def test(request):
    return  HttpResponse("Hello Test")

def about(request):
    return  HttpResponse("Hello About")

def page(request):
    return render(request ,"test.html")
