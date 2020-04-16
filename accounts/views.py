from django.shortcuts import render,redirect,HttpResponse
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
                print("Username Exist")
            elif User.objects.filter(email=email).exists():
                print("Email Exists")
            else:
                user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=pass1, email=email)
                user.save()
                print('User Created')
                
        else:
            print("Password Not matched")
            return HttpResponse("Password Not matched")
        return redirect('/accounts/')
       
    else:
         return render(request,'register.html')
       

def home(request):
    return render(request,'homepage.html')