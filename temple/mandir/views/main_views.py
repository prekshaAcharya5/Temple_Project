from django.shortcuts import render,get_object_or_404,redirect
from ..models import BeADonor
from ..models import AddDonor

def home(request):
    return render(request,'front/home.html')

def aboutus(request):
    return render(request,'front/aboutus.html')

def donor_form(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        address = request.POST.get("address")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        amount = request.POST.get("amount")
        donated_date = request.POST.get("donated_date")

        doner = BeADonor(name=name,address=address,phone_number=phone_number,email=email,amount=amount,donated_date=donated_date)
        doner.save()
        return redirect('home')

    return render(request,'front/beadoner.html')

def add_donor(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        address = request.POST.get("address")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        image = request.FILES.get("image")
        amount = request.POST.get("amount")
        donated_date = request.POST.get("donated_date")

        donors = AddDonor(name=name,address=address,phone_number=phone_number,email=email,image=image,amount=amount,donated_date=donated_date)
        donors.save()
        return redirect("home")
    
    return render(request,'front/add_doner.html')
    
def edit_donor(request,donor_id):
    donor = get_object_or_404(AddDonor, id=donor_id)

    if request.method == 'POST':
        donor.name = request.POST.get("name")
        donor.address = request.POST.get("address")
        donor.phone_number = request.POST.get("phone_number")
        donor.email = request.POST.get("email")
        donor.amount = request.POST.get("amount")
        donor.donated_date = request.POST.get("donated_date")
        donor.image = request.FILES.get("image")

        donor = AddDonor(name=donor.name,address=donor.address,phone_number=donor.phone_number,email=donor.email,image=donor.image,amount=donor.amount,donated_date=donor.donated_date) 
        donor.save()
        return redirect("home")
    
    return render(request,'front/edit_donor.html', {'donor':donor})


def event(request):
    
    return render(request,'front/event.html')

def gallery(request):
    return render(request,'front/gallery.html')

def member(request):
    return render(request,'front/member.html')

def create_committee_member(request):
    return render(request,"front/create_committee_member.html")


def notice(request):
    return render(request,'front/notice.html')
