from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from meetings.models import Meeting


# Create your views here.
def welcome(request):
    return render(request, "website/welcome.html", {"num_meetings": Meeting.objects.count()})


def date(request):
    return HttpResponse("Welcome to python programming " + str(datetime.now()))


def about(request):
    return HttpResponse("<input type='button' onclick='currentdate()' name='button'>test</input>")


def current_date():
    return str(datetime.now())
