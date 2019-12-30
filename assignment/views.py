from django.shortcuts import render,redirect
from .forms import *
from .models import *

def task_assign(request):
    task = TaskAssignment.objects.all()
    return render(request,'task.html',{'task':task})

def taskdone(request):
    task = Taskdone.objects.all()
    return render(request,'taskdone.html',{'task':task})
'''
def delete(reuest):
    task = TaskAssignment.objects.all()
    task.delete()
    return redirect('/task')
'''



