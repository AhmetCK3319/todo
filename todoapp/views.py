from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task

def addTask(request):
    # key bilgisini posta gönderiyoruz
    task=request.POST['task'] 
    # task model ile create ederek postu model aracılığı ile db gönderiyoruz
    Task.objects.create(task=task) 

    return redirect('home')
