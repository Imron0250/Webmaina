from django.shortcuts import render
from .models import *
import random

def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        print(name)
    data_1 = random.randint(1,200)
    data_2 = random.randint(1,200)
    data_3 = random.randint(1,200)
    data_4 = random.randint(1,200)
    context = {
        "info" : Info.objects.last(),
        'about' : About.objects.all().order_by('-id')[:2],
        'API' : API.objects.last(),
        'webmain' : Webmain.objects.all().order_by('-id')[:4],
        'text' : text.objects.last(),
        'blog' : Blog.objects.all().order_by('-id')[:3],
        'blog_text' : Blog_Text.objects.last(),
        'worker' : worker.objects.all().order_by('-id')[:6],
        'backround' : Backround.objects.last(),
        'youtube' : Youtube.objects.last(),
        'width' : Width.objects.last(),
        'data_1' : data_1,
        'data_2' : data_2,
        'data_3' : data_3,
        'data_4' : data_4,
        'result' : Result.objects.last(),
    

    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        "info" : Info.objects.last(),
        'about_us' : About_us.objects.last(),
        'worker' : worker.objects.all().order_by('-id')[:6],
        'backround' : Backround.objects.last(),
      
    }
    return render(request, 'about.html', context)

def faq(request):
    context = {
        "info" : Info.objects.last(),
        'faq' : Faq.objects.all().order_by('-id')[:3],
        'backround' : Backround.objects.last(),
  
    }
    return render(request, 'faq.html', context)
 
def blog(request):
    context = {
        "info" : Info.objects.last(),
        'backround' : Backround.objects.last(),
        'blog_site' : Blog_site.objects.all().order_by('-id')[:5],

    }
    return render(request, 'blog.html', context)

def contact(request):
    context = {
        "info" : Info.objects.last(),
        'digital_info' : Digital_Info.objects.last(),
        'backround' : Backround.objects.last(),

    }
    return render(request, 'contact.html', context)

def blog_sing(request, pk ):
    context = {
        'blog' : Blog.objects.get(id=pk),
        "info" : Info.objects.last(),

    }
    return render(request, 'blog-single.html', context)

def save(request):
    if request.method == "POST":
        name = request.POST.get("name")
        print(name)
    return render(request, 'save.html')