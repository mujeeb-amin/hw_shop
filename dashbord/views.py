from django.http import HttpResponse
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


# def home(request: WSGIRequest):

#     return HttpResponse("Home page")


def home(request: WSGIRequest):

    return render(request, "index.html")
