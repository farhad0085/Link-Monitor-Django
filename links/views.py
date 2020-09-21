from django.http.response import HttpResponse
from django.shortcuts import render


def home(request):

    return HttpResponse("Hello world")
