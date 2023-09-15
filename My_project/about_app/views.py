from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about(request):
    html = """
    <h1>Это страница обо мне</h1>
    <p>Я создаю свой первый сайт на Django.</p>
    """
    return HttpResponse(html)


def index(request):
    html = """
    <h1>Главная страница.</h1>
    <p>Это главная страница домашнего задания к 1-му семинару.</p>
    """
    return HttpResponse(html)
