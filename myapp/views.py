from django.shortcuts import render

# Create your views here.

def home(request):
    contaxt={'home':'active'}
    return render(request, 'myapp/home.html',contaxt)

def skill(request):
    skill={'skill':'active'}
    return render(request, 'myapp/skill.html' ,skill)

def contact(request):
    contact={'contact':'active'}
    return render(request, 'myapp/contact.html' ,contact)

def education(request):
    edu={'education':'active'}
    return render(request, 'myapp/education.html' ,edu)
