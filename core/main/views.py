from django.shortcuts import render, redirect
from .models import Logo, HomeInfo, Intro, Explain, Project, Picture, Contact, ContactUs
# Create your views here.


def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactUs.objects.create(name=name,email=email,message=message)
        return redirect('index')
    home_logo = Logo.objects.first()
    home_info = HomeInfo.objects.first()
    home_intro = Intro.objects.first()
    home_explain = Explain.objects.first()
    project = Project.objects.all()
    home_picture = Picture.objects.all()
    home_contact = Contact.objects.first()

    return render(request, 'main/index.html', context={
        'home_logo':home_logo,
        'home_info':home_info,
        'home_intro':home_intro,
        'home_explain':home_explain,
        'home_picture':home_picture,
        'project':project,
        'home_contact':home_contact
    })