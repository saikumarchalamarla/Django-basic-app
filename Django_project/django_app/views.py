from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hello(request):
    text='''<h1>Welcome to your first Django App.</h1>'''
    return HttpResponse(text)