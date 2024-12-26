from django.shortcuts import render, get_object_or_404
from apps.base.models import *
from django.http import HttpResponse
# My views

# Create your views here.
def index(request):
    try:
        about = About.objects.latest("id")
    except About.DoesNotExist:
        about = None    
    banner = Banner.objects.all()
    footer = Footer.objects.latest("id")
    news = News_item.objects.all()
    if request.method == 'POST':
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        adults = request.POST.get("adults")
        childs = request.POST.get("childs")
        result = Post.objects.create(fullname=fullname, phone=phone, date=date, adults=adults, childs=childs)
    return render(request, 'base/index.html', locals())

def about_us(request):
    uslugi = Uslugi.objects.all()
    footer = Footer.objects.latest("id")
    about = About.objects.latest("id")
    command = Command.objects.all()
    if request.method == 'POST':
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        adults = request.POST.get("adults")
        childs = request.POST.get("childs")
        result = Post.objects.create(fullname=fullname, phone=phone, date=date, adults=adults, childs=childs)
    return render(request, 'about.html', locals())

def news(request):
    footer = Footer.objects.latest("id")
    news = News.objects.all()
    if request.method =="POST":
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        adults = request.POST.get("adults")
        childs = request.POST.get("childs")
        result = Post.objects.create(fullname=fullname, phone=phone, date=date, adults=adults, childs=childs)
    return render(request, 'news2.html', locals())

def team(request):
    footer = Footer.objects.latest("id")
    commands = Commands.objects.all()
    if request.method == 'POST':
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        adults = request.POST.get("adults")
        childs = request.POST.get("childs")
        result = Post.objects.create(fullname=fullname, phone=phone, date=date, adults=adults, childs=childs)
    return render(request, 'team.html', locals())

def news_detail(request, id):
    footer = Footer.objects.latest("id")
    news = News_item.objects.latest("id")
    news = News_item.objects.get(id=id)
    if request.method == 'POST':
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        adults = request.POST.get("adults")
        childs = request.POST.get("childs")
        result = Post.objects.create(fullname=fullname, phone=phone, date=date, adults=adults, childs=childs)
    return render(request, 'detail/post.html', locals())

def news(request):
    footer = Footer.objects.latest("id")
    news = News_item.objects.all()
    if request.method == 'POST':
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        adults = request.POST.get("adults")
        childs = request.POST.get("childs")
        result = Post.objects.create(fullname=fullname, phone=phone, date=date, adults=adults, childs=childs)
    return render(request, 'news.html', locals())

def gallery(request):
    footer = Footer.objects.latest("id")
    gallery = Gallery.objects.all()
    if request.method == 'POST':
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        adults = request.POST.get("adults")
        childs = request.POST.get("childs")
        result = Post.objects.create(fullname=fullname, phone=phone, date=date, adults=adults, childs=childs)
    return render(request, 'gallery.html', locals())

def contact(request):
    footer = Footer.objects.latest("id")
    contact = Contact.objects.latest("id")
    if request.method == 'POST':
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        adults = request.POST.get("adults")
        childs = request.POST.get("childs")
        result = Post.objects.create(fullname=fullname, phone=phone, date=date, adults=adults, childs=childs)
    return render(request, 'contact.html', locals())