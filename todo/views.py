from django.shortcuts import render,redirect
from .forms import Todoforms
from .models import Todo



def index(request):
    context = {'todo_list':Todo.objects.all()}
    return render(request,"todo_list.html",context)


def form(request,id=0):
    if request.method == "GET":
        if id==0:
            form = Todoforms()
        else:
            user=Todo.objects.get(pk=id)
            form=Todoforms(instance=user)
        return render(request,'todo_form.html',{'form':form})
    else:
        if id==0:
            form = Todoforms(request.POST)
        else:
            user=Todo.objects.get(pk=id)
            form=Todoforms(request.POST,instance=user)
        if form.is_valid:
            form.save()
        return redirect('/index/')

def todo_del(request,id):
    user=Todo.objects.get(pk=id)
    user.delete()
    return redirect('/index/')
   

