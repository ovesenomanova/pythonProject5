from django.http import HttpRequest
from django.shortcuts import render


def hemingway(request: HttpRequest):
    return render(request, 'hemingway.html')


def shakespeare(request: HttpRequest):
    return render(request, 'shakespeare.html')