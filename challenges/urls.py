from django.urls import path
from . import views

urlpatterns = [
    path("control", views.index),
    path("hello", views.hello),
    path("IOb83bsjhd", views.secret),
    path("aG892kjs", views.noscape),
    path("home", views.home),
    path('<int:month>', views.monthly_challenge_by_number),
    path('<str:month>', views.monthly_challenge),
]
