from django.urls import path
from . import views

urlpatterns = [
    path('Hemingway/', views.hemingway),
    path('Shakespeare/', views.shakespeare)

]