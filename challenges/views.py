from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def index(request):
    return HttpResponse('<h1 style="color: green; background-color: white; font-family: Helvetica, sans-serif">You are under my control!</h1>')


def hello(request):
    return HttpResponse('<h1>This is hello page</h1><p><a href="control">Click me!</a></p>')


def secret(request):
    return HttpResponse('<h1 style="font-family: Helvetica, sans-serif">You found my little secret!</h1><a href="aG892kjs">My present for you!</a>')


def noscape(request):
    return HttpResponse('<h1 style="font-family:  Helvetica, sans-serif;">YOU HAVE NO ESCAPE!</h1><a href="control">Ok</a>')


def home(request):
    return HttpResponse('<h1 style="font-family: Helvetica, sans-serif" >Welcome to challenges!</h1><a href="IOb83bsjhd">Explore!</a>')


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = 'Eat no meat for the entire month!'
    elif month == 'feburary':
        challenge_text = 'Walk for at least 20 minutes every day!'
    elif month == 'march':
        challenge_text = 'Learn Django for at least 20 minutes every day!'
    else:
        return HttpResponseNotFound("This month is not supported.")
    return HttpResponse(challenge_text)
