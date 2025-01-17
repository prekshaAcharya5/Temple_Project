from django.shortcuts import render,redirect

def home(request):
    return render(request,'front/home.html')

def aboutus(request):
    return render(request,'front/aboutus.html')

def beadoner(request):
    return render(request,'front/beadoner.html')

def doner(request):
    return render(request,'front/doner.html')

def event(request):
    return render(request,'front/event.html')

def gallery(request):
    return render(request,'front/gallery.html')

def member(request):
    return render(request,'front/member.html')

def notice(request):
    return render(request,'front/notice.html')
