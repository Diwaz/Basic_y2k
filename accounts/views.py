from django.shortcuts import render,HttpResponse

def register(request):
    return render(request,'register.html')

def home(request):
    return render(request,'homepage.html')