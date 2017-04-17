from django.shortcuts import render
from django.http import HttpResponse
from Database.models import User

def index(request):
    user=User.objects.all()
    return HttpResponse("<h1>Jai Guru Umesh</h1>")