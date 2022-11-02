from multiprocessing import context
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Post

def index(request):

    db = Post.objects.all()
    context = {
        'title':'picah',
        'post': db
    }
    return render (request,'index.html', context);



# def index(request):
#     # return HttpResponse(" <h1> Hello, world. You're at the polls index.</h1>")
#     return render(request,'template/index.html')