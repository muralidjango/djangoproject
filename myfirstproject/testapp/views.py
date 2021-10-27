from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_word_view(arg):
    return HttpResponse("<center><h1>Hello Django</h1></center>")

def home_view(arg):
    return HttpResponse("<center><h1>This is home page</h1></center>")

def hello_pass_id_view(request, question_id):
    return HttpResponse("%s" % question_id)
