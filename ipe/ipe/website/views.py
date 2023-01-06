from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from things.models import Thing


# Create your views here.

def welcome(request):
    return render(request, "website/welcome.html", {"num_things": Thing.objects.all()})


def date(request):
    return HttpResponse("the page was served at " + str(datetime.now()))


def about(request):
    return HttpResponse("THis page is an about page and it contains the info about the app ipe")
