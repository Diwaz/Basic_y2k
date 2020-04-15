from django.shortcuts import render,redirect
from .forms import Todoforms
from .models import Todo



def index(request):
    return render(request,"base.html")


def form(request):
    form = Todoforms()
    return render(request,"todo_form.html",{'form':form})

