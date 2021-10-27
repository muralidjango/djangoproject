from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def second_view(arg):
        return HttpResponse("<h1>Hello Murali</h1>")
