from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task

def addTask(request):
    # key bilgisini posta gönderiyoruz
    task=request.POST['task'] 
    # task model ile create ederek postu model aracılığı ile db gönderiyoruz
    Task.objects.create(task=task) 

    return redirect('home')

def mark_as_done(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_complate=True
    task.save()
    return redirect('home')

def mark_as_undone(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.is_complate=False
    task.save()
    return redirect('home')

def edit_task(request,pk):
    get_task=get_object_or_404(Task,pk=pk)
    # metod post mu diye kontrol et
    if request.method =='POST':
        # metod post ise imput name alanı iste
        new_task=request.POST['task']
         # Task nesnesinin "task" alanını güncelle
        get_task.task=new_task
        # Değişikliği veritabanına kaydet
        get_task.save()
        # dönmek istediğin konuma git
        return redirect('home')
    else:    
        context={
            'get_task':get_task,
        }
        return render(request,'edit_task.html',context)

def delete_task(request,pk):
    get_task=get_object_or_404(Task,pk=pk)
    get_task.delete()
    return redirect('home')      