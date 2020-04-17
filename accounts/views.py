from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Exist")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Exist")
                return redirect("register")
            else:
                user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=pass1, email=email)
                user.save()
                print('User Created')
                
        else:
            messages.info(request,"Passwords Didn't Matched")
            return redirect("register")
        return redirect('/accounts/')
       
    else:
         return render(request,'register.html')
       

def home(request):
    return render(request,'homepage.html')

def login(request):
    return HttpResponse("LOGIN PAGE")