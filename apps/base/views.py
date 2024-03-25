from django.shortcuts import render
from apps.base.models import *
from django.http import HttpResponse


# Create your views here.
def index(request):
    banner = Banner.objects.all()
    facilties = Facilties.objects.all()
    services = Services.objects.all()
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

def team(request):
    commands = Commands.objects.all()
    if request.method == 'POST':
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        adults = request.POST.get("adults")
        childs = request.POST.get("childs")
        result = Post.objects.create(fullname=fullname, phone=phone, date=date, adults=adults, childs=childs)
    return render(request, 'team.html', locals())

def post(request, id):
    news = News.objects.get(id=id)
    if request.method == 'POST':
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        adults = request.POST.get("adults")
        childs = request.POST.get("childs")
        result = Post.objects.create(fullname=fullname, phone=phone, date=date, adults=adults, childs=childs)
    return render(request, 'detail/post.html', locals())

def news(request):
    news = News.objects.all()
    if request.method == 'POST':
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        adults = request.POST.get("adults")
        childs = request.POST.get("childs")
        result = Post.objects.create(fullname=fullname, phone=phone, date=date, adults=adults, childs=childs)
    return render(request, 'news.html', locals())


def gallery(request):
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
    contact = Contact.objects.latest("id")
    if request.method == 'POST':
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        adults = request.POST.get("adults")
        childs = request.POST.get("childs")
        result = Post.objects.create(fullname=fullname, phone=phone, date=date, adults=adults, childs=childs)
    return render(request, 'contact.html', locals())