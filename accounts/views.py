from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=pass1, email=email)
        user.save()
        print('User Created')
        return render(request,'todo_list.html')
       
    else:
         return render(request,'register.html')
       

def home(request):
    return render(request,'homepage.html')