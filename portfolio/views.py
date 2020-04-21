from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.

def home(request):
    projects = Project.objects.all()

    return render(request,'portfolio/home.html',{'projects':projects})

def pro1(request):
    return render(request,'portfolio/pro1.html')

def pro2(request):
    return render(request,'portfolio/pro2.html')

def pro3(request):
    return render(request,'portfolio/pro3.html')

def pro4(request):
    return render(request,'portfolio/pro4.html')

def pro5(request):
    return render(request,'portfolio/pro5.html')

def pro6(request):
    return render(request,'portfolio/pro6.html')

def pro7(request):
    return render(request,'portfolio/pro7.html')

def pro8(request):
    return render(request,'portfolio/pro8.html')
