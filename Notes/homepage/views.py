from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

def show_index(request):

    return render(request,'homepage/index.html')


def redirect_index(request):
    return HttpResponseRedirect("/home/index.html")

def redirect_None(request):
    return HttpResponseRedirect("/home/index.html")
