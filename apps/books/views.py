from django.shortcuts import render
from django.http import HttpRequest

def books(request: HttpRequest):
    return render(request, 'top.html')
