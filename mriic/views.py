from django.shortcuts import render,redirect
# Create your views here.
def  home(request):
    return render(request,'mriic/index.html')
    
def  aboutUs(request):
    return render(request,'mriic/aboutUs.html')







