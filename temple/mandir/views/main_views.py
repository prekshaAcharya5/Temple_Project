from django.shortcuts import render,redirect
from ..models import Committee,CommitteeMember,Content,ContentImage,Donor,DonorImage,ContactUs

def home(request):
    return render(request,'front/home.html')

def about_us(request):
    return render(request,'front/aboutus.html')

def be_a_doner(request):
    return render(request,'front/be_a_doner.html')

def doner(request):
    return render(request,'front/doner.html')

def event(request):
    return render(request,'front/event.html')

def gallery(request):
    return render(request,'front/gallery.html')

def committe(request):
    return render(request,'font/committe.html')

def add_member(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        post=request.POST.get('post')
        position=request.POST.get('position')
        image=request.FILES.get('committee_members')
        member=CommitteeMember.objects.create(
            name=name,
            address=address,
            post=post,
            position=position,
            image=image,
            c_id=request.c
        )
        member.save()
        return redirect('add_member')

    return render(request,'front/committe_member.html')

def committe_member(request):
    members=CommitteeMember.objects.all()
    return render(request,'front/committe_member')

def notice(request):
    return render(request,'front/notice.html')
