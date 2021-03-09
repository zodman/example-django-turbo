from django.shortcuts import render
from django.contrib import messages


def message(request):
    return render(request, "messages.html")


def index(request):
    messages.info(request, "message 2")
    return render(request, "index.html")
