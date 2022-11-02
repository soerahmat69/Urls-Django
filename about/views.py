from django.shortcuts import render

def index(request):
    return render (request,'about.html');

def recent(request):
    return render (request,'about.html');