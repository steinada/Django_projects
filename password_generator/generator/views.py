import string
from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    chars = list(string.ascii_lowercase*3)

    if request.GET.get("Uppercase"):
        chars.extend(list(string.ascii_uppercase*3))

    if request.GET.get("Special"):
        chars.extend(list(string.punctuation))

    if request.GET.get("Numbers"):
        chars.extend(list(string.digits))

    lenght = int(request.GET.get("lenght", 12))
    thepassword = "".join(random.sample(chars, lenght))

    return render(request, 'generator/password.html', {"password": thepassword})


def introduce(request):
    return render(request, 'generator/introduce.html')