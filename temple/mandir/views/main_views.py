from django.shortcuts import render,redirect,get_object_or_404
from ..models import Committee,CommitteeMember,Content,ContentImage,Donor,DonorImage,ContactUs
from django.http import HttpResponseBadRequest,HttpResponseNotFound

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

def add_committe(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        is_current = request.POST.get("is_current") == "on"
        Committee.objects.create(
            name=name,
            start_date=start_date,
            end_date=end_date,
            is_current=is_current,
        )
        return redirect('add_committe')
    return render(request, 'front/add_committe.html')

def committe(request):
    # Fetch all committees to display
    committees = Committee.objects.all()
    return render(request, 'front/committe.html', {'committees': committees})

def create_committee_member(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        post = request.POST.get('post')
        position = request.POST.get('position')
        image = request.FILES.get('image')  # Ensure the input name is 'image'
        c_id = request.POST.get('committee_id')
        committee = get_object_or_404(Committee, id=c_id)
        
        # Create and save the CommitteeMember instance
        committemember=CommitteeMember.objects.create(
            name=name,
            address=address,
            post=post,
            position=position,
            image=image,
            c_id=committee
        )
        committemember.save()
        return redirect('add_member')

    # Fetch committees for the dropdown
    committees = Committee.objects.all()
    return render(request, 'front/create_committee_member.html', {'committees': committees})
#  def create_committee_member(request):
#     if request.method == 'POST':
#         # Handle form submission (process POST data)
#         name = request.POST.get('name')
#         address = request.POST.get('address')
#         post = request.POST.get('post')
#         position = request.POST.get('position')
#         image = request.FILES.get('image')
#         committee_id = request.POST.get('committee_id')

#         # Validate committee existence
#         try:
#             committee = Committee.objects.get(id=committee_id)
#         except Committee.DoesNotExist:
#             return HttpResponseBadRequest("Invalid committee ID.")

#         # Create a new committee member
#         CommitteeMember.objects.create(
#             name=name,
#             address=address,
#             post=post,
#             position=position,
#             image=image,
#             c_id=committee
#         )
#         return HttpResponse("Committee member created successfully.")
    
#     elif request.method == 'GET':
#         # Render the form template
#         committees = Committee.objects.all()
#         return render(request, 'fronts/create_committee_member.html', {'committees': committees})
    
#     else:
#         return HttpResponseBadRequest("Invalid request method.")

def committe_member(request):
    members=CommitteeMember.objects.all()
    return render(request,'front/committe_member',{'members':members})

def notice(request):
    return render(request,'front/notice.html')
