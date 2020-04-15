from django.shortcuts import render,redirect
from .forms import Todoforms
from .models import Todo



def index(request):
    return render(request,"base.html")


def form(request):
    if request.method == "GET":
        form = Todoforms()
        return render(request,'todo_form.html',{'form':form})
    else:
        form = Todoforms(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/index/')
   

