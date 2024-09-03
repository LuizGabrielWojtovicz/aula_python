from django.shortcuts import render
from django.http import HttpResponse

def info(request):
    return HttpResponse('pagina info')

def blog(request):
    return HttpResponse('pagina blog')

def index(request):
    return HttpResponse('oi')